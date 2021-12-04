process.env.NODE_ENV = "test";

const request = require("supertest");
const db = require("../db");
const app = require("../app");

beforeAll(async () => {
    await db.run("CREATE TABLE IF NOT EXISTS activity(id TEXT, name TEXT)");
});

describe("GET / ", () => {
    test("It should return 200", async () => {
        const response = await request(app).get("/activity/");
        expect(response.statusCode).toBe(200);
    });

    test("It should return an array", async () => {
        const response = await request(app).get("/activity");
        expect(response.text).toEqual(JSON.stringify([]));
    });
});

describe("POST /", () => {
    test("IT should return 'Record Added'", async () => {
        const response = await request(app).post("/activity").send({
            id: 111,
            name: "Arsalan",
            date: "3 Mar 2019",
            time: 45,
            distance: 10,
        });
        expect(response.text).toEqual("Record Added!");
    });
});

describe("GET /asdf (invalid)", () => {
    test("It should return 404", async () => {
        const response = await request(app).get("/activity/asdf");
        expect(response.statusCode).toBe(404);
    });
});

afterAll(async () => {
    await db.run("DROP TABLE activity");
    db.close();
});
