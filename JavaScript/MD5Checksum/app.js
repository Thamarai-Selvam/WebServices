const express = require('express')
const app = express()
const bp = require('body-parser')

app.use(bp.text())

function md5(message) {

    var state = [0x67452301, 0xefcdab89, 0x98badcfe, 0x10325476]

    // Yet to Implement
}

app.get('/checksum', (req, res) => {

    var message = request.query.message
    return home(message, md5(message.encode("utf-8")).hex()), 200

    return res.send(genOTP)
})

//start 
app.listen(3000)