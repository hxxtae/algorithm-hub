const fs = require('fs');
const [N, K] = fs.readFileSync('/dev/stdin').toString().trim().split(' ').map(Number);
const maxlen = 100000;
const minlen = 0;
const visited = Array(maxlen + 1).fill(0);

function bfs() {
  const queue = [];
  queue.push([N, 0]); // [N, depth]
  visited[N] = 1;
  
  while (queue.length) {
    const [n, depth] = queue.shift();

    if (n === K) return depth;

    const check = [n - 1, n + 1, n * 2];
    
    for (let i = 0; i < 3; i++) {
      if (check[i] >= minlen && check[i] <= maxlen) {
        if (!visited[check[i]]) {
          if (check[i] === K) return depth + 1;
          visited[check[i]] = 1;
          queue.push([check[i], depth + 1]);
        }
      }
    }
  }
}

console.log(bfs());