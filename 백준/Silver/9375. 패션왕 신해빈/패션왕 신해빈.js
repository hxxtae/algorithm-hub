const fs = require('fs');
const stdin = fs.readFileSync('/dev/stdin').toString().trim();

// -------------
// 입력
// -------------
const input = stdin.split('\n').map(item => item.trim());
const LEN = input.length;
for (let i = 1; i < LEN;) {
  const N = +input[i++];
  const CLOTHES = input.slice(i, i + N);
  const result = solution(N, CLOTHES);
  console.log(result);
  i += N;
}

// -------------
// 풀이
// -------------
function solution(n, clothes) {
  const clothesMap = new Map();
  clothes.forEach((item) => {
    const category = item.split(' ')[1];
    clothesMap.set(category, (clothesMap.get(category) || 1) + 1);
  });

  let result = 1;
  clothesMap.forEach(val => result *= val);
  
  return result - 1;
}