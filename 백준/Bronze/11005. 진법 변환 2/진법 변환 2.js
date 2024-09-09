const fs = require('fs');
const [inputN, inputB] = fs.readFileSync('/dev/stdin').toString().trim().split(' ').map(Number);

function solution(n, b) {
  console.log(n.toString(b).toUpperCase());
}

solution(inputN, inputB);