const express = require('express')
const app = express()
const bp = require('body-parser')
const qrcode = require('qrcode')
app.use(bp.urlencoded({ extended: true }));

app.set('views', __dirname);
app.engine('html', require('ejs').renderFile);
app.set('view engine', 'ejs');

app.use(bp.text())


async function run(message, pres) {
    var src;
    await qrcode.toDataURL(message).then(res => {
        src = res

        pres.render('index.html', { value: message, img: src })
            // return src
    })

}

app.get('/qrcode', (req, res) => {

    var message = req.query.value


    run(message, res).catch(error => console.error(error.stack));
    // console.log(message, isrc)
    // res.render('index.html', { value: message, img: isrc })
    //return res.send(genOTP)
})


app.get('/', (req, res) => {

        res.render('index.html', { value: "message", img: "" });
    })
    //start 
app.listen(3000)