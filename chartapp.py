from flask import Flask, render_template, send_file, make_response
import sqlconnect
import json
from time import time
from ctolist import makecsv
from io import BytesIO
import matplotlib.pyplot as plt
import matplotlib

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('chart.html')
@app.route('/solar')
def solar():
    a = makecsv()
    b = []
    for i in range(len(a)):
        b.append(i)
    plt.figure(figsize=(10,10))
    plt.title("Solar Voltage")
    plt.plot(b, a, color='skyblue')
    img = BytesIO()
    plt.savefig(img, format="png",dpi=100)
    img.seek(0)
    return send_file(img, mimetype='image/png')
@app.route('/sensor-data')
def sensor():
    res = sqlconnect.sql()
    li = list(list_data['temp'] for list_data in res)
    li2 = list(id_data['id'] for id_data in res)

    x =  li2
    y = li
    data = [x,y]
    response = make_response(json.dumps(data))
    response.content_type = 'application/json'
    return response
if __name__ == "__main__":
    app.run(host="0.0.0.0", port="8080", debug='true')