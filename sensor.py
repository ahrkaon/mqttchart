import time
import paho.mqtt.client as mqtt
import json
import pymysql

broker = "localhost"
recvData = ""

#define callback
def on_message(client, userdata, message):
    mydb = pymysql.connect(host="localhost",port=3306,user="root",password="password",db="Monitor",charset="utf8")
    curs = mydb.cursor()

    time.sleep(1)
    recvData = str(message.payload.decode("utf-8"))
    print("Recieved message = ",recvData)
    jsonData = json.loads(recvData)
    print("Temp : "+str(jsonData["Temp"]))
    print("Pres : "+str(jsonData["Pres"]))
    mytemp = str(jsonData["Temp"])
    mypres = str(jsonData["Pres"])
    print(mytemp)
    print(mypres)
    sql = """INSERT INTO sensorvalue(temp, pres) VALUES (%s, %s)"""
    val = (mytemp,mypres)
    curs.execute(sql,val)
    mydb.commit()


client = mqtt.Client()
client.on_message=on_message

while True:
    print("connecting to broker ",broker)
    client.connect(broker)
    client.loop_start()
    print("subscribing")
    client.subscribe("Sensor")
    time.sleep(5)
    client.disconnect()
    client.loop_stop()
    time.sleep(10)

