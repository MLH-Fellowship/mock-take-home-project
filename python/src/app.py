from flask import Flask, Response, jsonify, request, abort
import json 
import re

app = Flask(__name__)

date_regex = re.compile("\d{4}-\d{2}-\d{2}")
#activities = [{"date": "2021-12-01", "name":"Cycling", "duration": 45, "distance": 10}]
activities = []

def is_valid(activity: dict) -> bool:
    date = activity.get("date", "")
    if re.match(date_regex,date) is None:
        return False  
    try:
        name = activity.get("name")
        duration = activity.get("duration")
        distance = activity.get("distance")
        #jassert isinstance(duration, int)
        #assert isinstance(distance, int)
    except:
        return False
    return True

@app.route('/')
def index():
    return "Welcome to Sports Hub!", 200

@app.route('/activity', methods=['GET', 'POST'])
def activity():
    if request.method == "GET":
        return jsonify(activities)

    elif request.method == "POST":
        activity = request.get_json()
        app.logger.info(activity)
        if activity is None or not is_valid(activity):
            abort(400)
        activities.append(activity)
        return "Record Added!", 200
    else:
        return "Error!", 400



if __name__ == "__main__":
    app.run(debug=True)