const fs = require('fs');
const { off } = require('process');
const input = fs.readFileSync('/dev/stdin').toString().trim().split('\n');
const [N, M, V] = input[0].trim().split(' ').map(Number);
const ARR = [];
const visited1 = new Array(N + 1).fill(0);
const visited2 = new Array(N + 1).fill(0);

for (let i = 0; i <= N; i++) {
  ARR.push([...new Array(N + 1).fill(0)]);
}

for (let i = 1; i <= M; i++) {
  const [a, b] = input[i].trim().split(' ').map(Number);
  ARR[a][b] = ARR[b][a] = 1;
}

const stack = [];
const queue = [];
const resultStr = [];

function dfs(idx) {
  visited1[idx] = 1;

  stack.push(idx);
  for (let i = 1; i <= N; i++) {
    if (!visited1[i] && ARR[idx][i] !== 0) {
      dfs(i);
    }
  }
  return;
}

function bfs(idx) {
  const arr = [];

  visited2[idx] = 1;
  queue.push(idx);
  arr.push(idx);
  
  while (arr.length) {
    idx = arr.shift();
    for (let i = 1; i <= N; i++) {
      if (!visited2[i] && ARR[idx][i] !== 0) {
        visited2[i] = 1;
        queue.push(i);
        arr.push(i);
      }
    }
  }
  return;
}

dfs(V);
bfs(V);
resultStr.push(stack.join(' '));
resultStr.push(queue.join(' '));
console.log(resultStr.join('\n'));