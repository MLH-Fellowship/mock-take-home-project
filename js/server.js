const express = require("express");
const app = express();
const port = 3000;

const activities = [
  {
    id: 0,
    date: "2022-03-04",
    name: "Running",
    duration: 60,
    distance: 4.3,
  },
  {
    id: 1,
    date: "2022-03-06",
    name: "Cycling",
    duration: 120,
    distance: 25,
  },
];

app.get("/", (req, res) => {
  res.send("Welcome to Sports Hub!");
});

app.get("/activities", (req, res) => {
  // Complete me
  res.send("Record Fetched!");
});

app.post("/activities", (req, res) => {
  // Complete me
  // Add a new activitiy to the activites array
  res.send("Add record!");
});

app.put("/activities/:id", (req, res) => {
  // Complete me
  // Change the data for an activity inside of the activities array
  res.send("Activity changed!");
});

app.delete("/activities/:id", (req, res) => {
  // Complete me
  // Delete an activity inside of the activities array
  res.send("Activity deleted!");
});

app.listen(port, () => {
  console.log(`App listening on port ${port}`);
});
