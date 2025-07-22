const fs = require("fs");
const input = fs.readFileSync("dev/stdin").toString().trim();

// 알파벳 26개
const alphabets = new Array(26).fill(0);

// 아스키 코드 변환 후 +
for (word of input) {
  const wordIdx = word.charCodeAt(0) - 97;
  alphabets[wordIdx]++;
}

console.log(alphabets.join(" "));
