from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "Welcome to Sports Hub!"

@app.route('/activity', methods=['GET', 'POST'])
def activity():
    return "Record Added!"
