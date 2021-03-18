function compress(uncompressed) {
  // Initialize dictionary
  let dictionary = {};
  for (let i = 0; i < 256; i++) {
    dictionary[String.fromCharCode(i)] = i;
  }

  let word = "";
  let result = [];
  let dictSize = 256;

  for (let i = 0, len = uncompressed.length; i < len; i++) {
    let curChar = uncompressed[i];
    let joinedWord = word + curChar;

    // Do not use dictionary[joinedWord] because javascript objects
    // will return values for myObject['toString']
    if (dictionary.hasOwnProperty(joinedWord)) {
      word = joinedWord;
    } else {
      result.push(dictionary[word]);
      // Add wc to the dictionary.
      dictionary[joinedWord] = dictSize++;
      word = curChar;
    }
  }

  if (word !== "") {
    result.push(dictionary[word]);
  }

  return result;
}

function decompress(to_compressed) {
  compressed = [];
  for (i = 0; i < to_compressed.length; i++) {
    compressed.push(parseInt(to_compressed[i]));
  }
  //   console.log(compressed);
  // Initialize Dictionary (inverse of compress)
  let dictionary = {};
  for (let i = 0; i < 256; i++) {
    dictionary[i] = String.fromCharCode(i);
  }
  let word = String.fromCharCode(compressed[0]);
  let result = word;
  //   console.log(result);
  let entry = "";
  let dictSize = 256;

  for (let i = 1, len = compressed.length; i < len; i++) {
    let curNumber = compressed[i];

    if (dictionary[curNumber] !== undefined) {
      entry = dictionary[curNumber];
    } else {
      if (curNumber === dictSize) {
        entry = word + word[0];
      } else {
        throw "Error in processing";
        return null;
      }
    }

    result += entry;

    // Add word + entry[0] to dictionary
    dictionary[dictSize++] = word + entry[0];

    word = entry;
  }
  //   console.log(result);
  return result;
}

exports.compress = compress;
exports.decompress = decompress;
