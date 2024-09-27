const fs = require('fs');
const stdin = fs.readFileSync('/dev/stdin').toString().trim();

// -------------
// 입력
// -------------
const input = stdin.split('\n').map(item => item.trim().split(' ').map(Number));
const [[N], ...TREE] = input;

// -------------
// 입력
// -------------
function solution(n, tree) {
  const graph = Array.from({ length: n + 1 }, () => []);
  for (const [a, b] of tree) {
    graph[b].push(a); // NOTE: b -> a 방향 (문제와 반대로)
  }

  const dfs = (node, cnt) => {
    for (const next of graph[node]) {
      cnt = dfs(next, cnt + 1);
    }

    return cnt;
  }

  for (let i = 1; i <= n; i++) {
    const count = dfs(i, 1);
    if (count === n) return i;
  }

  return -1;
}

// -------------
// 입력
// -------------
const result = solution(N, TREE);
console.log(result);