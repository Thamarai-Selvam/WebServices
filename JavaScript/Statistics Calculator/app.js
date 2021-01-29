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

function lrReg(X, Y) {

    const sumX = X.reduce((accumulator, value) => accumulator + value, 0)
    const sumY = Y.reduce((accumulator, value) => accumulator + value, 0)
    const sumXX = X.reduce((accumulator, value) => accumulator + value * value, 0)

    let sumXY = 0;
    for (let i = 0; i < X.length; i++) {
        sumXY += X[i] * Y[i];
    }
    console.log(sumX, sumY, sumXX, sumXY)

    // ANY ONE ARRAY LENGTH
    const n = X.length

    const a = ((sumY * sumXX) - (sumX * sumXY)) / ((n * sumXX) - (sumX * sumX))
    const b = ((n * sumXY) - (sumX * sumY)) / ((n * sumXX) - (sumX * sumX))

    // REGRESSSION EQUATION => Y = a + bx
    return `${a} + ${b} (x)`
}


app.get('/statcalc', (req, res) => {

    console.log(req.query)



    var opChoice = parseInt(req.query.opChoice)
    console.log('data', data, 'data1', data1);

    if (opChoice == 0) {
        var data = req.query.data.split(',').map(Number)
        var result = variance(data)
    } else if (opChoice == 1) {
        var data = req.query.data.split(',').map(Number)
        var result = stdDev(data)
    } else {
        var data1 = req.query.data1.split(',').map(Number)
        var data2 = req.query.data2.split(',').map(Number)
        var result = lrReg(data1, data2)
    }

    // res.render('index.html', { data: data, data1: data1, data2: data2, result: result })
    res.send({ data: data, data1: data1, data2: data2, result: result })

})


app.get('/', (req, res) => {

    res.render('index.html', { data: "1,2,3,4,5,6", data1: "1,2,3,4,5,6", data2: "1,2,3,4,5,6", result: "" })
})

app.listen(3000)