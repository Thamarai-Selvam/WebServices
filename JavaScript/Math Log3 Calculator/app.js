const express = require('express')
const app = express()
const bp = require('body-parser')
app.use(bp.urlencoded({ extended: true }));

app.set('views', __dirname);
app.engine('html', require('ejs').renderFile);
app.set('view engine', 'ejs');
app.use(bp.text())
const PI = 3.141592653589793;

function roundnum2(x, p) {
    var i;
    var n = parseFloat(x);
    var m = n.toFixed(p);
    var y = String(m);
    i = y.length;
    j = y.indexOf('.');
    if (i > j && j != -1) {
        while (i > 0) {
            if (y.charAt(--i) == '0')
                y = removeAt(y, i);
            else
                break;
        }
        if (y.charAt(i) == '.')
            y = removeAt(y, i);
    }
    return y;
}

function removeAt(s, i) {
    s = s.substring(0, i) + s.substring(i + 1, s.length);
    return s;
}

function getsin(number) {

    number %= 2 * PI;
    if (number < 0) {
        number = 2 * PI - number;
    }

    let sign = 1;
    if (number > PI) {
        number -= PI;
        sign = -1;
    }

    let PRECISION = 50;
    let temp = 0;
    for (let i = 0; i <= PRECISION; i++) {
        temp += Math.pow(-1, i) * (Math.pow(number, 2 * i + 1) / fact(2 * i + 1));
    }
    result = sign * temp;
    return result
}

function getCos(number) {
    number = (PI / 2) - number;
    return getsin(number)

}

function fact(num) {
    if (num == 0 || num == 1)
        return 1;
    else
        return num * fact(num - 1);
}


function getTrigResult(x, op, degType) {

    var y;
    if (op <= 5 && degType == 0) x *= Math.PI / 180;
    if (op == 0) y = getsin(x); //y = Math.sin(x);
    else if (op == 1) y = getCos(x);
    else if (op == 2) y = getsin(x) / getCos(x);
    else if (op == 3) y = 1 / getsin(x);
    else if (op == 4) y = 1 / getCos(x);
    else if (op == 5) y = getCos(x) / getsin(x);
    else if (op == 6) y = Math.asin(x);
    else if (op == 7) y = Math.acos(x);
    else if (op == 8) y = Math.atan(x);
    else if (op == 9) y = Math.asin(1 / x);
    else if (op == 10) y = Math.acos(1 / x);
    else y = Math.atan(1 / x);
    if (op >= 6 && degType == 0) y *= 180 / Math.PI;
    y = roundnum2(y, 8);
    return y;
}
app.get('/log3', (req, res) => {

    console.log(req.query)

    op = req.query.opChoice
    degType = req.query.degType
    data = req.query.data

    result = getTrigResult(data, op, degType)
    if (result)
        res.render('index.html', { data: data, num: data, degType: degType, result: result })
    else
        res.status(500).send('Invalid Data !')




})


app.get('/', (req, res) => {
    res.render('index.html', { data: "1", num: "", degType: "deg", result: "" });
})

app.listen(3000)