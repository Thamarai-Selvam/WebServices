const express = require('express')
const app = express()
const bp = require('body-parser')
app.use(bp.urlencoded({ extended: true }));

app.set('views', __dirname);
app.engine('html', require('ejs').renderFile);
app.set('view engine', 'ejs');
app.use(bp.text())

app.post('/ecalc', (req, res) => {

    console.log(req.body)

    vChoice = req.body.vChoice
    aChoice = req.body.aChoice
    a = req.body.num
    v = req.body.num1



    if (aChoice == 0)
        a /= 1000
    else if (aChoice == 1)
        a = a
    else
        a *= 1000
    if (vChoice == 0)
        v /= 1000
    else if (vChoice == 1)
        v = v
    else
        v *= 1000

    iw = a * v
    ikw = a * v / 1000
    imw = a * v * 1000
        // res.send({ 'Operation': vOpName, 'i/p data': data, 'result': vresult })
        // res.send({ Operation: vOpName, data: data, pow: pow, base: base, num: data, num3: data, result: vresult })
    res.render('index.html', { num: req.body.num, num1: req.body.num1, w: iw, kw: ikw, mw: imw });

})


app.get('/', (req, res) => {
    res.render('index.html', { num: "", num1: "", w: "", kw: "", mw: '' });
})

app.listen(3000)