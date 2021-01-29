const express = require('express')
const app = express()
const bp = require('body-parser')
app.use(bp.urlencoded({ extended: true }));

app.set('views', __dirname);
app.engine('html', require('ejs').renderFile);
app.set('view engine', 'ejs');
app.use(bp.text())

function nLog(x) {
    var n = 99999999
    return n * ((x ** (1 / n)) - 1)
}

function log(x, base) {

    var result = nLog(x) / nLog(base)
    return result

}

function antiLog(a, b) {

    var c = 1;
    for (var i = 1; i <= b; i++) {
        c = c * a;
    }
    return c;
}


app.get('/log1', (req, res) => {

    console.log(req.query)

    op = req.query.opChoice
    if (op == 0) {
        var data = req.query.num3
        var base = req.query.base
        console.log('data', data);

        var vOpName = "Log";
        var vresult = log(data, base)
    } else if (op == 1) {
        var data = parseInt(req.query.num)

        var vresult = nLog(data)
        var vOpName = "Natural Log";

    } else if (op == 2) {
        var data = parseInt(req.query.data)
        var pow = parseInt(req.query.pow)
        var vresult = antiLog(data, pow)
        var vOpName = "AntiLog";
    } else {
        res.status(500).send('Invalid Data !')
    }

    // res.send({ 'Operation': vOpName, 'i/p data': data, 'result': vresult })
    // res.send({ Operation: vOpName, data: data, pow: pow, base: base, num: data, num3: data, result: vresult })
    res.render('index.html', { data: data, pow: pow, base: base, num: data, num3: data, opName: vOpName, result: vresult });

})


app.get('/', (req, res) => {
    res.render('index.html', { data: "1,2", pow: "", base: "", num: "", num3: "", opName: "Result", result: "" });
})

app.listen(3000)