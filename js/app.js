const bodyParser = require("body-parser");
var express = require("express");
const Sqlite = require("sqlite3");
var app = express();
const userRoutes = require("./routes/user");

app.use("/activity/", userRoutes);

// const db = new Sqlite.Database("database/activity.db");
// db.run(
//   "CREATE TABLE IF NOT EXISTS activity(date DATE, name TEXT, time TIME, distance TEXT)"
// );

app.use(bodyParser.json());

module.exports = app;
