
import requests
import pymysql

API_KEY = 'SE123xazASfasd221279843saghdkjsaERuoicncvmx'

dbHost = 'localhost'
dbUser = 'user'
dbPass = 'pass'
dbNamne = 'database name'

try:
    db_connection = pymysql.connect(host=dbHost, user=dbUser, password=dbPass, database=dbNamne)
    cursor = db_connection.cursor()
    print("connected !!!!")
except Exception as e:
    print(f"error connecting: {e}")
    exit()

API_URL = 'https://api.example.com/data'

try:
    response = requests.get(API_URL, params={'api_key': API_KEY})
    data = response.json()
    print("recieved data succesfully!!")
except Exception as e:
    print(f"error when recieving : {e}")
    exit()

try:
    for item in data:
        sql = "INSERT INTO students (age, name ) VALUES (%s, %s)"
        cursor.execute(sql, (12, 'Ali'))
    db_connection.commit()
    print("inserted successfully!")
except Exception as e:
    db_connection.rollback()
    print(f"Error occured: {e}")

db_connection.close()
