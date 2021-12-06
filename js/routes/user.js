const express = require("express");
const router = express.Router();

router.get("/", function (req, res) {
  res.send("Hello World");
});

// router.post("/", (res, req) => {
//   co
// });

module.exports = router;
