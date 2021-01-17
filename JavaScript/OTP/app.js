const express = require('express')
const app = express()
const bp = require('body-parser')

app.use(bp.text())


app.get('/otp', (req, res) => {

    var length = parseInt(req.query.length)
    var typeOfOtp = parseInt(req.query.typeotp)

    if (typeOfOtp == 0)
        typeContents = "1234567890"
    else if (typeOfOtp == 1)
        typeContents = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    else
        typeContents = "1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

    var genOTP = "",
        i;
    console.log(typeOfOtp, typeContents)
    for (i = 0; i < length; i++) {
        genOTP += typeContents[Math.floor(Math.random() * typeContents.length)]
    }

    return res.send(genOTP)
})

//start 
app.listen(3000)