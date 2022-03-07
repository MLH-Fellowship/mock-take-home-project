# Mock Take Home Project - APIs

This template repository will be used for the Mock Take Home Project. Every time you push a change, a set of tests will be run against your code. 

You can chose to write this in JavaScript or Python. There will be 4 tests for each language, meaning there will be 8 tests. You only need to get 4 tests from the same language to pass. You're welcome to complete this in both languages to get additional practice!

## Prompt

We're going to be building an API for a Sports Hub. They want to track daily sport activities record, for example running or cycling times.

We need an API that can process the track records. We'll need to build one!

## Track Record

Each track record should have the following fields:
- Date of activity
- Activity name (Running, Cycle)
- Time duration (e.g. 45 minutes)
- Distance (e.g. 10 kilometers)

## Tests

There's a number of tests we need to pass. These include:
- Successfully respond with a 200
- Records should return list activities as array
- New command should return newly added activities
- An API call to any of the command with incomplete value should return 400.

Tests have been provided already. A database is not required for this example, and you should use a data structure inside your code to store data during the autograder.

You may be required to implement a database in a real take home project so it's encouraged you practice those.

To run the Python tests, run the following commands inside of the `python` directory:
```
cd python && sudo -H pip3 install pytest
pytest
```

To run the JavaScript tests, run the following commands inside of the `js` directory:

```
cd js && npm install
npm test
```

## Submission

Commit and push your changes to GitHub and it will get autograded. Once 4 of the tests from one of the languages passes, you've completed it!

We will be checking solutions to ensure they aren't using harcoded values. At the end of the day, this exercise is to help you!