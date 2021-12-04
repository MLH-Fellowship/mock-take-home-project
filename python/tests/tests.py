import pytest
import requests

def test_status():
    assert 200 == requests.get('http://127.0.0.1:5000').status_code

def test_response():
    assert type([]) == type(requests.get('http://localhost:5000/activity').json())
    assert [] == requests.get('http://localhost:5000/activity').json()

def test_post():
    assert "Record Added!" == requests.post('http://localhost:5000/activity', json={"date": "2021-12-01", "name":"Cycling", "duration": 45, "distance": 10}).text

# TODO: An API call to any of the command with incomplete value should return 400.
def test_incomplete():
    assert 404 == requests.get('http://localhost:5000/activity/fdkjal').status_code

def test_invalid_activity():
    resp = requests.post('http://localhost:5000/activity', json={"date":"1234", "name":"excited basketweaving"})
    assert resp.status_code == 400
