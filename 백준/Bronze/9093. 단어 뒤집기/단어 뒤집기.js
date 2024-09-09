const fs = require('fs');
const stdin = fs.readFileSync('/dev/stdin').toString().trim().split('\n');
const inputCnt = +stdin.shift().trim();
const inputArr = stdin.map(item => item.trim().split(' '));

function solution(cnt, arr) {
  const newStrArr = [];
  for (str of arr) {
    const newStr = str
      .map(item => item
        .split('')
        .reverse()
        .join(''))
      .join(' ');
    newStrArr.push(newStr);
  }
  return printResult(newStrArr);
}

function printResult(resultArr) {
  return resultArr.join('\n');
}

console.log(solution(inputCnt, inputArr));