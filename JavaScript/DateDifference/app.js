const express = require('express')
const app = express()
const bp = require('body-parser')

app.use(bp.text())

app.get('/datediff', (req, res) => {
    var Months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    var fromDateSet = []
    var toDateSet = []
    var diffDateSet = []
    var index = []
    console.log(req.query)

    if ((1000 <= req.query.fromYear <= 9999) && (1000 <= req.query.toYear <= 9999))
        if ((1 <= req.query.fromMonth <= 12) && (1 <= req.query.fromMonth <= 12))
            if ((1 <= req.query.fromDate <= 31) && (1 <= req.query.toDate <= 31))
                if ((0 <= req.query.fromHour < 24) && (0 <= req.query.toHour < 24))
                    if ((0 <= req.query.fromMinute < 60) && (0 <= req.query.toMinute < 60))
                        if ((0 <= req.query.fromSeconds < 60) && (0 <= req.query.toSeconds < 60)) {} else res.send('Invalid Seconds !')
    else res.send('Invalid Minutes !')
    else res.send('Invalid Hours !')
    else res.send('Invalid Date !')
    else res.send('Invalid Month !')
    else res.send('Invalid Year !')

    if (req.query.toSeconds >= req.query.fromSeconds)
        diffDateSet.push(req.query.toSeconds - req.query.fromSeconds)
    else {
        diffDateSet.push((req.query.toSeconds + 60) - req.query.fromSeconds)
        req.query.toMinute -= 1
    }


    if (req.query.toMinute >= req.query.fromMinute)
        diffDateSet.push(req.query.toMinute - req.query.fromMinute)
    else {
        diffDateSet.push((req.query.toMinute + 60) - req.query.fromMinute)
        req.query.toHour -= 1
    }


    if (req.query.toHour >= req.query.fromHour)
        diffDateSet.push(req.query.toHour - req.query.fromHour)
    else {
        diffDateSet.push((req.query.toHour + 24) - req.query.fromHour)
        req.query.toDate -= 1
    }


    if (req.query.toDate >= req.query.fromDate)
        diffDateSet.push(req.query.toDate - req.query.fromDate)
    else {
        diffDateSet.push((req.query.toDate + Months[req.query.toMonth]) - req.query.fromDate)
        req.query.toMonth -= 1
    }


    if (req.query.toMonth >= req.query.fromMonth)
        diffDateSet.push(req.query.toMonth - req.query.fromMonth)
    else {
        diffDateSet.push((req.query.toMonth + 12) - req.query.fromMonth)
        req.query.toYear -= 1
    }


    if (req.query.toYear >= req.query.fromYear)
        diffDateSet.push(req.query.toYear - req.query.fromYear)
    else
        diffDateSet.push(0)

    var resultDiff = diffDateSet[5] + ' Years' + diffDateSet[4] + ' Months' + diffDateSet[3] + ' Days' + diffDateSet[2] + ' Hours' + diffDateSet[1] + ' Minutes' + diffDateSet[0] + ' Seconds'




    res.send(resultDiff);
})

//start 
app.listen(3000)