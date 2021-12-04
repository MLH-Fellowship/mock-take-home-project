const express = require("express");
const bodyParser = require("body-parser");

const activityRouter = require("./activity");
const db = require("./db");

const app = express();
db.run(
    "CREATE TABLE IF NOT EXISTS activity(id INT NOT NULL PRIMARY KEY, name TEXT, date TEXT, time INT, distance INT)"
);

app.use(bodyParser.json());
app.use("/activity", activityRouter);

module.exports = app;
