const express = require("express");
const router = express.Router();

router.get("/", function (req, res) {
  var sql = "select * from activity";
  var params = [];
  db.all(sql, params, (err, rows) => {
    if (err) {
      res.status(400).json({ error: err.message });
      return;
    }
    res.json({
      message: "success",
      data: rows,
    });
  });
});

router.post("/", (res, req) => {
  var errors = [];

  var data = {
    name: req.body.name,
    date: req.body.date,
    time: req.body.time,
    distance: req.body.distance,
  };
  var sql = "INSERT INTO user (date, name, time, distance) VALUES (?,?,?,?)";
  var params = [data.date, data.name, data.time, data.distance];
  db.run(sql, params, function (err, result) {
    if (err) {
      res.status(400).json({ error: err.message });
      return;
    }
    res.json({
      message: "success",
      data: data,
    });
  });
});

module.exports = router;
