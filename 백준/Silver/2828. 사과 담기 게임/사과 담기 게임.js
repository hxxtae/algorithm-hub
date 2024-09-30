const fs = require('fs');
const input = fs.readFileSync("./dev/stdin").toString().trim().split('\n');

const [N, M] = input.shift().split(' ').map(Number);
input.shift();
const apples = input.map(Number)

let left = 1;
let right = M;
let move = 0;

for (let i = 0; i < apples.length; i++) {
  const apple = apples[i];
  if (apple >= left && apple <= right) continue;
  else if (apple < left) {
    const dist = left - apple;
    left = apple;
    right = right - dist;
    move += dist;
  } else {
    apple > right
    const dist = apple - right;
    right = apple;
    left = left + dist;
    move += dist;
  }
}
console.log(move)