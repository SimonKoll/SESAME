const express = require('express')
const bodyParser = require('body-parser')
const app = express()
app.set('view engine', 'ejs')
const MongoClient = require('mongodb').MongoClient
connstring = 'mongodb+srv://sesame:sesame2021@cluster0.5zncd.mongodb.net/myFirstDatabase?retryWrites=true&w=majority'

app.use(bodyParser.urlencoded({ extended: true }))
app.use(function(req, res, next) {

    // Website you wish to allow to connect
    res.setHeader('Access-Control-Allow-Origin', 'http://localhost:4200');

    // Request methods you wish to allow
    res.setHeader('Access-Control-Allow-Methods', 'GET, POST, OPTIONS, PUT, PATCH, DELETE');

    // Request headers you wish to allow
    res.setHeader('Access-Control-Allow-Headers', 'X-Requested-With,content-type');

    // Set to true if you need the website to include cookies in the requests sent
    // to the API (e.g. in case you use sessions)
    res.setHeader('Access-Control-Allow-Credentials', true);

    // Pass to next layer of middleware
    next();
});
MongoClient.connect(connstring, { useUnifiedTopology: true })
    .then(client => {
        console.log('Connected to Database')
        const db = client.db('entrants')
        const entrantCollection = db.collection('entrants')
            // All your handlers here...

        app.delete('/delete-entrants', (req, res) => {
            entrantCollection.findOneAndDelete({ "id": req.body(id) })
        })
        app.post('/entrants', (req, res) => {
                entrantCollection.insertOne(req.body)
                    .then(result => {
                        res.redirect('/')
                    })
                    .catch(error => console.error(error))
            })
            // We normally abbreviate `request` to `req` and `response` to `res`.
        app.get('/get-entrant', function(req, res) {
            db.collection('entrants').find().toArray()
                .then(results => {
                    console.log("retrieving Entrants successful")
                    res.send(results)
                })
                .catch(error => console.error(error))
                // do something here
        })
        app.get('/get-unknown', function(req, res) {
            db.collection('unknown').find().toArray()
                .then(results => {
                    console.log("retrieving unknown Entrants")
                    res.send(results)
                })
                .catch(error => console.error(error))
                // do something here
        })
    }).catch(console.error)




app.listen(3000, function() {
    console.log('listening on 3000')
})