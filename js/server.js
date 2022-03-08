const app = require("./app");
const db = require("./db");

// Create db table
db.run("CREATE TABLE IF NOT EXISTS activity(id TEXT AUTO_INCREMENT, date DATETIME, name TEXT, time INTEGER, distance INTEGER)");

app.get("/", async (req, res) => {
    res.sendStatus(200);
});

// Record an activity
app.post("/activity/", async (req, res) => {
    const params = req.params;
    if (!(params.date && params.name && params.time && params.distance)) {
        res.sendStatus(400);
    } else {
        await db.run(`INSERT INTO activity(${params.date}, ${params.name}, ${params.time}, ${params.distance})`);
        res.status(200).send("Record Added!");
    }
});

// Return an array of activities
app.get("/activity/", async (req, res) => {
    const records = await db.run(`SELECT * FROM activity`);
    res.status(200).send(records);
});