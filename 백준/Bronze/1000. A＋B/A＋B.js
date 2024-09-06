const fs = require('fs');
const [a, b] = fs.readFileSync("/dev/stdin").toString().trim().split(" ");

console.log(Number(a)+Number(b))