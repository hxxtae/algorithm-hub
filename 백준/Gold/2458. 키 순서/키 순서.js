const fs = require('fs');
const stdin = fs.readFileSync('/dev/stdin').toString().trim();

// -------------
// 입력
// -------------
const input = stdin.split('\n').map(item => item.trim().split(' ').map(Number));
const [[N, M], ...RELATION] = input;

// -------------
// 풀이 (DFS)
// -------------
function solution(n, m, relation) {
  const graph = Array.from({ length: n + 1 }, () => Array(n + 1).fill(Infinity));
  for (const [a, b] of relation) {
    graph[a][b] = 1;
  }
  
  for (let k = 1; k <= n; k++) {
    for (let r = 1; r <= n; r++) {
      for (let c = 1; c <= n; c++) {
        if (graph[r][c] > graph[r][k] + graph[k][c]) {
          graph[r][c] = graph[r][k] + graph[k][c];
        }
      }
    }
  }

  let result = 0;
  for (let r = 1; r <= n; r++) {
    let cnt = 0;
    for (let c = 1; c <= n; c++) {
      if (graph[r][c] !== Infinity || graph[c][r] !== Infinity) 
        cnt++;
    }
    if (cnt === n - 1)
      result++;
  }
  return result;
}

// -------------
// 출력
// -------------
const result = solution(N, M, RELATION);
console.log(result)
