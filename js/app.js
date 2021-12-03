const express = require("express");
const bodyParser = require("body-parser");

const activityRouter = require("./activity");

const app = express();

app.use(bodyParser.json());
app.use("/activity", activityRouter);

module.exports = app;
