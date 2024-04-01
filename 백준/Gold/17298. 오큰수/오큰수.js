const fs = require('fs');
const stdin = fs.readFileSync('/dev/stdin').toString().trim().split('\n');
const inputCnt = +stdin.shift();
const inputArr = stdin[0].trim().split(' ').map(Number);

function solution(cnt, arr) {
  const stack = [0];
  for (let i = 1; i < cnt; i++) {
    if (arr[i - 1] < arr[i]) {
      while (stack.length && arr[stack[stack.length - 1]] < arr[i]) {
        arr[stack.pop()] = arr[i];
      }
    }
    stack.push(i);
  }
    
  while (stack.length) {
    arr[stack.pop()] = -1;
  }
    
  console.log(arr.join(' '));
}

solution(inputCnt, inputArr);