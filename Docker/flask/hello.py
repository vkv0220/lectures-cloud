from flask import Flask
import requests
import json
import os, sys
import psycopg2

app = Flask(__name__)
param=os.environ.get('NAME')
api_key=os.environ.get('API_KEY')

request_string=f"https://api.openweathermap.org/data/2.5/weather?id=1489425&lang=ru&units=metric&appid={api_key}"

response = requests.get(request_string)
res_text = json.loads(response.text)
print(res_text['name'])
print(res_text['main']['temp'])
print(param)
print(sys.argv[1])

@app.route('/')
def hello():
    conn = psycopg2.connect(
    host="db",
    database="app_db",
    user="app_user",
    password="app_pass")
    cur = conn.cursor()
    #cur.execute('SELECT version()')
    cur.execute('CREATE TABLE IF NOT EXISTS apptable (id SERIAL PRIMARY KEY, value VARCHAR(255) NOT NULL)')
    sql = f"INSERT INTO apptable (value) VALUES ( { res_text['main']['temp'] } )"
    cur.execute(sql)

    cur.execute('SELECT * FROM apptable')

    datalist = []
    rows = cur.fetchall()
    for row in rows:
        datalist.append(row)

        cur.close()
        conn.commit()

    return f'<div> Привет, { param } </div> <div> Погода сегодня. В: { res_text["name"] } температура воздуха: { res_text["main"]["temp"] } </div><p>{str(datalist)}</p>'
