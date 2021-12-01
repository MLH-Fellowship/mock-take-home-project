import pytest
import requests

def test_status():
    assert 200 == requests.get('http://127.0.0.1:5000').status_code

def test_response():
    assert type([]) == type(requests.get('http://localhost:5000/activity').json())
    assert [] == requests.get('http://localhost:5000/activity').json()

def test_post():
    assert "Record Added!" == requests.post('http://localhost:5000/activity', data={"date": "2021-12-01", "name":"Cycling", "duration": 45, "distance": 10}).text
