const Sqlite = require("sqlite3");
// eslint-disable-next-line no-undef
const dbName =
    process.env.NODE_ENV === "test" ? "activity_test.db" : "activity.db";
const db = new Sqlite.Database(`database/${dbName}`);

module.exports = db;
