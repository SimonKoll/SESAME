const express = require("express");
const app = express();
app.use(express.static("public"));

app.get('/', (req, res) => {
    res.sendFile(__dirname + "/public/" + "login_register.html");
})

app.listen(3000, function() {
    console.log("Running on port 3000.");
});