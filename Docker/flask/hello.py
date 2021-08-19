from flask import Flask
import requests
import json
import os, sys
import psycopg2

app = Flask(__name__)
param=os.environ.get('NAME')
api_key=os.environ.get('API_KEY')

request_string=f"https://api.openweathermap.org/data/2.5/weather?id=1489425&lang=ru&units=metric&appid={api_key}"
# conn = psycopg2.connect(
#             host=os.environ.get('DBHOST'),
#             database="postgres",
#             user="postgres",
#             password="postgres")

response = requests.get(request_string)
res_text = json.loads(response.text)
print(res_text['name'])
print(res_text['main']['temp'])
print(param)
print(sys.argv[1])
# print('PostgreSQL database version:')
# cur.execute('SELECT version()')

@app.route('/')
def hello():
    print(str(response))
    return f'<div> Привет, { param } </div> <div> Погода сегодня. В: { res_text["name"] } температура воздуха: { res_text["main"]["temp"] } </div>'
