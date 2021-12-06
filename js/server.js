const app = require("./app");

const port = 3000;
app.listen(port, () => {
    console.log(`Server started on Port :${port}`);
});

app.get('/', (req, res) => {
    res.status(200).send({"message" : "work success"});
});