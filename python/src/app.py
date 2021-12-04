import json
from flask import Flask, jsonify, request
import logging
from db import create_tables, get_db

app = Flask(__name__)


@app.route('/')
def hello():
    return 'Hello World'

# NOT WORKING


@ app.route('/activity', methods=['POST'])
def activity():
    db = get_db()
    data = request.get_data()
    data = json.loads(data)
    db.execute('INSERT INTO activity (date, name, duration, distance) VALUES (?, ?, ?, ?)',
               (data['date'], data['name'], data['duration'], data['distance']))
    db.commit()
    msg = "Record Added!"
    return msg, 200


@ app.route('/activity', methods=['GET'])
def activities():
    db = get_db()
    activities = db.execute('SELECT * FROM activity').fetchall()
    return jsonify(activities)


if __name__ == "__main__":
    create_tables()
    app.run(host='127.0.0.1', port=5000, debug=True)
