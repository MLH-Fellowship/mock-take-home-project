from flask import Flask, Response, jsonify, request, abort, g
from contextlib import closing
import json 
import re
import sqlite3

DATABASE = 'sporthub.db'

app = Flask(__name__)

def connect_db():
    return sqlite3.connect(app.config['DATABASE'])

def init_db():
    with app.app_context():
        db = get_db()
        with app.open_resource('schema.sql', mode='r') as f:
            db.cursor().executescript(f.read())
        db.commit()

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    return db

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()


def is_valid(activity: dict) -> bool:
    date_regex = re.compile("\d{4}-\d{2}-\d{2}")
    date = activity.get("date", "")
    if re.match(date_regex, date) is None:
        return False  
    try:
        name = activity.get("name")
        duration = activity.get("duration")
        distance = activity.get("distance")
        assert name is not None
        assert isinstance(duration, int)
        assert isinstance(distance, int)
    except:
        return False
    return True

@app.route('/')
def index():
    return "Welcome to Sports Hub!", 200

@app.route('/activity', methods=['GET', 'POST'])
def activity():
    db = get_db()
    if request.method == "GET":
        cur = db.execute("SELECT date,duration,distance,name FROM activities")
        entries = [{"date":row[0],"duration":row[1],"distance":row[2],"name":row[3]} for row in cur.fetchall()]
        return jsonify(entries), 200

    elif request.method == "POST":
        activity = request.get_json()
        app.logger.info(activity)
        if activity is None or not is_valid(activity):
            abort(400)
        args = (activity["date"], activity["duration"], activity["distance"], activity["name"] )
        db.execute("INSERT INTO activities(date,duration,distance,name) values (?,?,?,?)", args)
        db.commit()
        return "Record Added!", 200
    else:
        return "Error!", 400


if __name__ == "__main__":
    app.config["DATABASE"] = DATABASE
    app.run(debug=True)