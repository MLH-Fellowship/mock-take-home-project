const express = require("express");
const router = express.Router();

router.get("/", (req, res) => {
    res.send("GET Activities");
});

router.post("/", (req, res) => {
    res.send("POST Activity");
});

router.delete("/:id", (req, res) => {
    res.send("DELETE Activity");
});

module.exports = router;
