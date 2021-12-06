from flask import Flask, request, jsonify
import json
import sqlite3

app = Flask(__name__)

@app.route('/')
def index():
    return "Welcome to Sports Hub!"

def create_table(conn):
    conn.cursor().execute("""
        CREATE TABLE IF NOT EXISTS
        activities(
            name TEXT,
            date TEXT,
            duration INTEGER,
            distance INTEGER
        )
    """)

def connection():
    conn = None
    try:
        conn = sqlite3.connect('activity.db')
    except Exception as ex:
        print(ex)
    return conn

@app.route('/activity', methods=['POST', 'GET'])
def activity():
    conn = connection()
    cursor = conn.cursor()
    #create table
    create_table(conn)

    if request.method == 'GET':
        try:
            data = cursor.execute("select * from activities")
            result = cursor.fetchall()
            toReturn = []
            for row in result:
                toReturn.append({
                    "name":row[0],
                    "date":row[1],
                    "duration":row[2],
                    "distance":row[3]
                })
            return jsonify(toReturn),200
        except Exception as ex:
            print("woopsies, something went wrong lol")
            return "error", 400
    else:
        try:
            req = request.get_json()
            data = (req["name"], req["date"], req["duration"], req["distance"])
            cursor.execute("INSERT INTO activities VALUES(?,?,?,?)",data)
            conn.commit()
        except Exception as ex:
            print("woopsies, something went wrong lol")
            return "error", 400

        return "Record Added!", 200
    

