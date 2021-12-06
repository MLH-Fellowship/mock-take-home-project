var express = require("express");
var app = express();
const userRoutes = require("./routes/user");

app.use("/activity/", userRoutes);

exports.modules = app;
