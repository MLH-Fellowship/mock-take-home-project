from flask import Flask

app = Flask(__name__)

activities = [
    {
        "id": 0,
        "date": "2022-03-04",
        "name": "Running",
        "duration": 60,
        "distance": 4.3
    },
    {
        "id": 1,
        "date": "2022-03-06",
        "name": "Cycling",
        "duration": 120,
        "distance": 25
    }
]

@app.route('/')
def home():
    return "Welcome to Sports Hub!"

@app.route('/activities', methods=['GET'])
def get_activities():
    # Complete me
    return "Record Added!"

@app.route('/activities/new', methods=['GET'])
def add_activity():
    # Complete me
    # Add a new activity to the activities array
    return "Add record!"

@app.route('/activities/change/<id>', methods=['GET'])
def change_activity(id):
    # Complete me
    # Change the data for an activity inside of the activities array
    return "Activity changed!"

@app.route('/activities/delete/<id>', methods=['GET'])
def delete_activity(id):
    # Complete me
    # Delete an activity inside of the activities array
    return "Activity deleted!"
