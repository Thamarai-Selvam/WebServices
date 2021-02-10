const express = require('express')
const app = express()
const bp = require('body-parser')
app.use(bp.urlencoded({ extended: true }));
const co = require('./code128.js')
app.set('views', __dirname);
app.engine('html', require('ejs').renderFile);
app.set('view engine', 'ejs');

app.use(bp.text())


app.get('/barcode', (req, res) => {

    var message = req.query.value
        // var src = bc.BarCodeCreation(message, 50, 1, 10)
        //res.render('index.html', { value: message, img: isrc })
        //return res.send(genOTP)
    var code = new co.Code128(message)
    code = code.insert().toDataURL()
    console.log(code)
    res.render('index.html', { value: message, img: code });
})


app.get('/', (req, res) => {

        res.render('index.html', { value: "message", img: "" });
    })
    //start 
app.listen(3000)