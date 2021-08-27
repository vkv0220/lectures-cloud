from flask import Flask
import requests
import json
import os
import psycopg2

app = Flask(__name__)
param = os.environ.get('NAME')
api_key = os.environ.get('API_KEY')
api_url = "https://api.openweathermap.org/data/2.5/"

req_str = f"{api_url}weather?id=1489425&lang=ru&units=metric&appid={api_key}"

response = requests.get(req_str)
res_text = json.loads(response.text)


def connect():

    """ Connect to the PostgreSQL database server """
    conn = None
    try:
        conn = psycopg2.connect(
            host="db",
            database="app_db",
            user="app_user",
            password="app_pass")
        cur = conn.cursor()
        datalist = []
# cur.execute('SELECT version()')
        cur.execute('CREATE TABLE IF NOT EXISTS apptable \
        (id SERIAL PRIMARY KEY, value VARCHAR(255) NOT NULL)')
        sql = f"INSERT INTO apptable (value) VALUES \
        ({ res_text['main']['temp'] })"
        cur.execute(sql)

        cur.execute('SELECT * FROM apptable')
        rows = cur.fetchall()
        for row in rows:
            datalist.append(row)
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
    return datalist


@app.route('/')
def hello():
    datalist = connect()
    return f'<div> Привет, { param } </div> <div> Погода сегодня. \
    В: { res_text["name"] } температура воздуха: { res_text["main"]["temp"] } \
    </div><p>{str(datalist)}</p>'
