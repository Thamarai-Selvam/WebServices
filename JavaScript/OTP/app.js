const express = require('express')
const app = express()
const bp = require('body-parser')
app.use(bp.urlencoded({ extended: true }));

app.set('views', __dirname);
app.engine('html', require('ejs').renderFile);
app.set('view engine', 'ejs');

app.use(bp.text())


app.get('/otp', (req, res) => {

    var length = parseInt(req.query.length)
    var typeOfOtp = parseInt(req.query.typeotp)

    if (typeOfOtp == 0)
        typeContents = "1234567890"
    else if (typeOfOtp == 1)
        typeContents = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    else
        typeContents = "1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

    var genOTP = "",
        i;
    console.log(typeOfOtp, typeContents)
    for (i = 0; i < length; i++) {
        genOTP += typeContents[Math.floor(Math.random() * typeContents.length)]
    }

    res.render('index.html', { length: length, typeotp: typeOfOtp, response: genOTP })
        //return res.send(genOTP)
})


app.get('/', (req, res) => {

        res.render('index.html', { length: 6, typeotp: 0, response: "" });
    })
    //start 
app.listen(3000)