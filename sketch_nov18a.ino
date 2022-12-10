#include <ArduinoJson.h>
#include <Wire.h>
#include <Adafruit_BMP085.h>
#include <ESP8266WiFi.h>
#include <PubSubClient.h>
#define seaLevelPressure_hPa 1013.25

Adafruit_BMP085 bmp;

const char* ssid = "CJWiFi_FD61";
const char* password = "2001003505";
const char* mqtt_server = "192.168.200.140";

WiFiClient espClient;
PubSubClient client(espClient);
unsigned long lastMsg = 0;
#define MSG_BUFFER_SIZE  (50)
char msg[MSG_BUFFER_SIZE];
int value = 0;

// 센서값 json 직렬화(json 형태로 변환)
void MyJson(float temp, float pres)
{
  DynamicJsonDocument  doc(300); 
  doc["Temp"]=temp;
  doc["Pres"]=pres;

  Serial.print("Json Data :");
  serializeJson(doc,Serial);
  Serial.println();
  serializeJson(doc, msg);
}
void setup_wifi() {

  delay(10);
  // We start by connecting to a WiFi network
  Serial.println();
  Serial.print("Connecting to ");
  Serial.println(ssid);

  WiFi.mode(WIFI_STA);
  WiFi.begin(ssid, password);

  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }

  randomSeed(micros());

  Serial.println("");
  Serial.println("WiFi connected");
  Serial.println("IP address: ");
  Serial.println(WiFi.localIP());
}

void callback(char* topic, byte* payload, unsigned int length) {
  Serial.print("Message arrived [");
  Serial.print(topic);
  Serial.print("] ");
  for (int i = 0; i < length; i++) {
    Serial.print((char)payload[i]);
  }
  Serial.println();

  // Switch on the LED if an 1 was received as first character
  if ((char)payload[0] == '1') {
    digitalWrite(BUILTIN_LED, LOW);   // Turn the LED on (Note that LOW is the voltage level
    // but actually the LED is on; this is because
    // it is active low on the ESP-01)
  } else {
    digitalWrite(BUILTIN_LED, HIGH);  // Turn the LED off by making the voltage HIGH
  }

}

void reconnect() {
  // Loop until we're reconnected
  while (!client.connected()) {
    Serial.print("Attempting MQTT connection...");
    // Create a random client ID
    String clientId = "ESP8266Client-";
    clientId += String(random(0xffff), HEX);
    // Attempt to connect
    if (client.connect(clientId.c_str())) {
      Serial.println("connected");
      // Once connected, publish an announcement...
      client.publish("outTopic", "hello world");
      // ... and resubscribe
      client.subscribe("inTopic");
    } else {
      Serial.print("failed, rc=");
      Serial.print(client.state());
      Serial.println(" try again in 5 seconds");
      // Wait 5 seconds before retrying
      delay(5000);
    }
  }
}
void setup() {
  // put your setup code here, to run once:
  Serial.begin(115200);
  if(!bmp.begin())
  {
    Serial.println("BMP180 Not Found. Check Circuit");
  }
  setup_wifi();
  client.setServer(mqtt_server, 1883);
  client.setCallback(callback);

}

void loop() {
  // put your main code here, to run repeatedly:
  delay(2000);
  double t = bmp.readTemperature();
  double p = bmp.readPressure();

  MyJson(t,p);

  if(!client.connected())
  {
    reconnect(); 
  }
  client.loop();

  long now = millis(); // 현재시간 - 과거시간(시작시간)
  if(now - lastMsg > 2000)
  {
    lastMsg = now;
    Serial.print("Publish message:");
    Serial.print(msg);
    client.publish("Sensor",msg);
  }
  delay(2000);

}
