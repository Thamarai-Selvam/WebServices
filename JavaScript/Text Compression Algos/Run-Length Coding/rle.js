function rleCompression(text) {
  var encoding = "";

  var i = 0;

  while (i < text.length) {
    let count = 1;
    while (i + 1 < text.length && text[i] == text[i + 1]) {
      count = count + 1;
      i = i + 1;
    }

    encoding += String(count) + text[i];
    i = i + 1;
  }
  console.log(encoding);
  return encoding;
}

function run_length_decoding(encoding) {
  var result = "";
  var cnt = 0;
  var num = "";
  var no = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"];
  for (var i = 0; i < encoding.length; i++) {
    if (no.includes(encoding[i])) {
      num = num.concat(encoding[i]);
    } else {
      while (cnt < parseInt(num)) {
        result = result.concat(encoding[i]);
        cnt += 1;
      }
      num = "";
      cnt = 0;
      // console.log(result);
    }
  }
  return result;
}

exports.rleCompression = rleCompression;
exports.run_length_decoding = run_length_decoding;
