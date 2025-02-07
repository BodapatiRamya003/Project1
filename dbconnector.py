import sqlite3
from sqlite3 import Error

def connect_db(path):
    connection =none
    try:
        connection =sqlite3.connect(path)
        print ("connection establish")
    except Error as e:
        print (e)
    return connection

