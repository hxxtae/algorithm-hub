const fs = require('fs');
const input = fs.readFileSync('/dev/stdin').toString().trim().split('\n');
const N = +input[0];
const ARR = Array.from({ length: N + 1 }, () => []);
const visited = Array.from({ length: N + 1 }, () => 0);
const M = input.length - 1;
for (let i = 1; i < M; i++) {
  const [a, b] = input[i].trim().split(' ').map(Number);
  ARR[a].push(b);
  ARR[b].push(a);
}
const parent = Array.from({ length: N + 1 }, () => -1);
const compare_list = input[M].trim().split(' ').map(Number);

function bfs(idx) {
  const queue = [];
  visited[idx] = 1;
  queue.push(idx);
  let prev = 1;
  
  while (queue.length) {
    const temp = queue.shift();
    visited[temp] = 1;
    let cnt = 0;
    for (num of ARR[temp]) {
      if (!visited[num]) {
        parent[num] = temp;
        cnt++;
      }
    }
    for (let childcnt = 0; childcnt < cnt; childcnt++) {
      if (parent[compare_list[prev + childcnt]] !== temp) {
        return 0;
      }
      queue.push(compare_list[prev + childcnt]);
    }
    prev += cnt;
  }
  return 1;
}

function solution() {
  const result = bfs(1);
  console.log(result ? 1 : 0);
}

solution();