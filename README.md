# Mock Take Home Project - APIs

This template repository will be used for the Mock Take Home Project.

There's a Python and JavaScript repository to give you something to work with. You should use the language most used with your project.

## Prompt

We're going to be building an API for a Sports Hub. They want to track daily sport activities record, for example running or cycling times.

We need an API that can process the track records. We'll need to build one!

## Track Record

Each track record should have the following fields:
- ID (integer, e.g. 1)
- Date of activity (YYYY-MM-DD, e.g. 2022-03-08)
- Activity name (String .g. Running, Cycle)
- Time duration (integer in minutes e.g. 45 minutes)
- Distance (float in kilometers e.g. 10 kilometers)

## Tests

There's a number of test cases we need to ensure work. These include:
- Successful API calls will respond with a 200 status
- GET `/activities` records should return list activities as an array
- POST `/activities` will add a new activities to the array
- PUT `/activities/<id>` will add a modify an activity in the array
- DELETE `/activities/<id>` will add a delete activities in the array
- API calls with incorrect inputs (wrong input variables or data types) will return a 400 status

You are **required to write tests** to ensure your solution works. A database is not required for this example but you're encouraged to add one to help build your skillset!

## Submission

You'll be making your own version of this using GitHub Classroom.

 - [] Commit and push your changes to this repository. 
 - [] Make a Pull Request so that your Pod Leader can leave feedback on when you're ready. 
 - [] Invite your pod leader to the repository and tag them in your Pull Request when you're ready to get feedback.
