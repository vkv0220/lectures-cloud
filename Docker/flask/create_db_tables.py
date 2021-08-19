import psycopg2
#from config import config
import os, sys

dbuser=os.environ.get('DBUSER')
dbpass=os.environ.get('DBPASS')

def create_db_tables():

    """ create tables in the PostgreSQL database"""
    commands = (
        """
        CREATE DATABASE flask_app_db;
        """,
        """
        CREATE TABLE flask_app (
            id SERIAL PRIMARY KEY
        )
        """)
    conn = None
    try:
        # read the connection parameters
        #params = config()
        # connect to the PostgreSQL server
        conn = psycopg2.connect(
            host=db,
            database="flask_app_db",
            user=dbuser,
            password=dbpass)
        cur = conn.cursor()
        # create table one by one
        for command in commands:
            cur.execute(command)
        # close communication with the PostgreSQL database server
        cur.close()
        # commit the changes
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()


if __name__ == '__main__':
    create_db_tables()
