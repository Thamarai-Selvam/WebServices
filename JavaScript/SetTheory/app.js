const express = require('express')
const app = express()
const bp = require('body-parser')

app.use(bp.text())

Set.prototype.union = function(otherSet) {
    var unionSet = new Set();
    for (var elem of this) {
        unionSet.add(elem);
    }
    for (var elem of otherSet)
        unionSet.add(elem);

    return unionSet;
}

Set.prototype.intersection = function(otherSet) {
    var intersectionSet = new Set();
    for (var elem of otherSet) {
        if (this.has(elem))
            intersectionSet.add(elem);
    }
    return intersectionSet;
}
Set.prototype.minus = function(otherSet) {
    var differenceSet = new Set();
    for (var elem of this) {
        if (!otherSet.has(elem))
            differenceSet.add(elem);
    }
    return differenceSet;
}
app.get('/setops', (req, res) => {

    var operation = req.query.operation
    var setA = new Set(req.query.setA)
    var setB = new Set(req.query.setB)

    console.log(req.query)
    if (operation == 0) {
        console.log(setA.union(setB))
        return res.send({ 'Union': [...setA.union(setB)] });
    } else if (operation == 1) {
        console.log(setA.intersection(setB))
        return res.send({ 'Intersection': [...setA.intersection(setB)] });
    } else {
        console.log(setA.minus(setB))
        return res.send({ 'Minus': [...setA.minus(setB)] });
    }

})

//start 
app.listen(3000)