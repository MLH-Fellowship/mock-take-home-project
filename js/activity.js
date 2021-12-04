const express = require("express");
const db = require("./db");

const router = express.Router();

router.get("/", async (req, res) => {
    db.all("SELECT * FROM activity", function (err, allRows) {
        if (err) {
            res.send("Something went unexpected!");
            return console.log("Something went unexpected!", err.message);
        }
        return res.send(allRows);
    });
});

router.post("/", (req, res) => {
    console.log(req.body);
    db.serialize(() => {
        db.run(
            "INSERT INTO activity(id,name,date,time,distance) VALUES(?,?,?,?,?)",
            [
                req.body.id,
                req.body.name,
                req.body.date,
                req.body.time,
                req.body.distance,
            ],
            (err) => {
                if (err) {
                    res.send("Something went unexpected!\n" + err);
                    return console.log("Something went unexpected!\n" + err);
                }
                return res.send("Record Added!");
            }
        );
    });
});
router.delete("/:id", (req, res) => {
    res.send("DELETE Activity");
});

module.exports = router;
