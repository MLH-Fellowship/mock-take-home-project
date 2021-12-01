# Python Edition

## Setup

```
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Run

### Run the API

```
export FLASK_APP=src/app.py
flask run
```

### Run the tests (while the API is already running)

```
pytest tests/tests.py
```
