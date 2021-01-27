const express = require('express')
const app = express()
const bp = require('body-parser')
app.use(bp.urlencoded({ extended: true }));

app.set('views', __dirname);
app.engine('html', require('ejs').renderFile);
app.set('view engine', 'ejs');
app.use(bp.text())


function variance(arr) {
    const mean = arr.reduce((acc, val) => acc + val, 0) / arr.length
    return arr
        .reduce((acc, val) => acc.concat((val - mean) ** 2), [])
        .reduce((acc, val) => acc + val, 0) / arr.length

}

function stdDev(arr) {
    return Math.sqrt(variance(arr))

}

function lrReg(arr) {
    return arr

}
app.get('/statcalc', (req, res) => {

    console.log(req.query)


    var data = req.query.data.split(',').map(Number)
    console.log('data', data);

    varn = variance(data)
    stDev = stdDev(data)
    lReg = lrReg(data)

    res.render('index.html', { data: data, variance: varn, stDev: stDev, lReg: "-" })

})


app.get('/', (req, res) => {

    res.render('index.html', { data: "1,2,3,4,5,6", variance: 0, stDev: 0, lReg: "-" });
})

app.listen(3000)