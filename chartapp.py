from flask import Flask, render_template, url_for, request, make_response
import sqlconnect
import json
from time import time

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('chart.html')

@app.route('/sensor-data')
def sensor():
    res = sqlconnect.sql()
    li = list(list_data['temp'] for list_data in res)
    li2 = list(id_data['id'] for id_data in res)

    #data = li
    #data2 = li2
    #total = [data2, data]
    x =  li2
    y = li
    data = [x,y]
    response = make_response(json.dumps(data))
    response.content_type = 'application/json'
    return response
if __name__ == "__main__":
    app.run(host="0.0.0.0", port="8080", debug='true')