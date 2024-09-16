const fs = require('fs');
const stdin = fs.readFileSync('/dev/stdin').toString().trim();

// -------------
// 입력
// -------------
const input = stdin.split('\n').map(item => item.trim().split(' ').map(Number));
const [X] = input.pop();
const [[N, M], ...WORKS] = input;

// -------------
// 풀이 (DFS)
// -------------
function solution2(n, m, x, works) {
  const visited = Array(n + 1).fill(0);
  const graph = Array.from({ length: n + 1 }, () => []);
  for (const [a, b] of works) {
    graph[b].push(a);
  }
  
  const dfs = (node, cnt) => {
    visited[node] = 1;
    for (const next of graph[node]) {
      if (visited[next]) continue;
      cnt = dfs(next, cnt + 1);
    }

    return cnt;
  }

  return dfs(x, 0);
}

// -------------
// 출력
// -------------
const result2 = solution2(N, M, X, WORKS);
console.log(result2);