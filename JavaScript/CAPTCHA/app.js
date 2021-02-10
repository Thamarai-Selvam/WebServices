const express = require('express')
const app = express()
const bp = require('body-parser')
app.use(bp.urlencoded({ extended: true }));

app.set('views', __dirname);
app.engine('html', require('ejs').renderFile);
app.set('view engine', 'ejs');
const { createCanvas, loadImage } = require('canvas')
app.use(bp.text())



app.get('/captcha', (req, res) => {

    var code = req.query.value
    var tCtx = createCanvas(code.length * 30, 50).getContext('2d')
    var newElem = code;
    var colors = ['red', 'green', 'blue', 'orange', 'yellow'];
    tCtx.font = '22pt "Calibri"';
    tCtx.fillText(newElem, 10, 30);
    tCtx.beginPath()
    for (let index = 0; index < code.length; index++) {
        tCtx.strokeStyle = colors[Math.floor(Math.random() * colors.length)];
        tCtx.lineTo(Math.floor(Math.random() * code.length * 50), Math.floor(Math.random() * code.length))
        tCtx.lineTo(Math.floor(Math.random() * code.length), Math.floor(Math.random() * code.length * 50))
        tCtx.stroke()
    }


    var src = tCtx.canvas.toDataURL();


    res.render('index.html', { value: code, img: src })
        //return res.send(genOTP)
})


app.get('/', (req, res) => {

        res.render('index.html', { value: "message", img: "" });
    })
    //start 
app.listen(3000)