const express = require('express')
const app = express()
const bp = require('body-parser')
app.use(bp.urlencoded({ extended: true }));

app.set('views', __dirname);
app.engine('html', require('ejs').renderFile);
app.set('view engine', 'ejs');
app.use(bp.text())

function rgcf(x, y) {

    if (x == 0)
        return y
    return rgcf(y % x, x)
}

function gcf(data) {

    var tempRes = data[0]
    data.forEach(element => {
        tempRes = rgcf(element, tempRes)
    });
    if (tempRes == 1)
        return 1
    return tempRes

}

function rlcm(x, y) {
    return (!x || !y) ? 0 : Math.abs((x * y) / rgcf(x, y));
}

function lcm(data) {
    var tempRes = data[0]
    data.forEach(element => {
        tempRes = rlcm(element, tempRes)
    });
    if (tempRes == 1)
        return 1
    return tempRes
}

function sqrt(data) {
    var sqrt = data / 2;
    var temp = 0;

    while (sqrt != temp) {
        temp = sqrt;
        sqrt = (data / temp + temp) / 2;
    }
    return sqrt
}

function crt(data) {
    var i, precision = 0.000001,
        n = data;

    for (i = 1;
        (i * i * i) <= n; ++i); //Integer part

    for (--i;
        (i * i * i) < n; i += precision); //Fractional part

    return i;
}

function nrt(data) {
    var x = data[0],
        n = data[1];
    return (((x > 1 || x < -1) && n == 0) ? Infinity : ((x > 0 || x < 0) && n == 0) ? 1 : (x < 0 && n % 2 == 0) ? `${((x < 0 ? -x : x) ** (1 / n))}${"i"}` : (n == 3 && x < 0) ? -Math.cbrt(-x) : (x < 0) ? -((x < 0 ? -x : x) ** (1 / n)) : (n == 3 && x > 0 ? Math.cbrt(x) : (x < 0 ? -x : x) ** (1 / n)));
}

app.get('/log2', (req, res) => {

    console.log(req.query)

    op = req.query.opChoice
    if (op == 0) {
        var data = req.query.data.split(',').map(Number)
        console.log('data', data);

        var vOpName = "GCF and LCM";
        var vresult = gcf(data) + " and " + lcm(data)
    } else if (op == 1) {
        var data = parseInt(req.query.data)

        var vresult = sqrt(data) + ' and ' + crt(data)
        var vOpName = "Square Root and Cube Root";

    } else if (op == 2) {
        var data = req.query.data.split(',').map(Number)
        var vresult = nrt(data)
        var vOpName = "Nth Root";
    } else {
        res.status(500).send('Invalid Data !')
    }

    res.render('index.html', { data: data, opName: vOpName, result: vresult })

})


app.get('/', (req, res) => {
    res.render('index.html', { data: "1,2,3,4,5,6", opName: "vv", result: "" });
})

app.listen(3000)