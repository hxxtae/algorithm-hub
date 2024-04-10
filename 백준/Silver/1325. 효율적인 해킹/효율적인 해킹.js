const fs = require('fs');
const stdin = fs.readFileSync('/dev/stdin').toString().trim();

// -------------
// 입력
// -------------
const input = stdin.split('\n').map(item => item.trim().split(' ').map(Number));
const [[N, M], ...CONN] = input;

// -------------
// 풀이 (BFS)
// -------------
function solution1(n, m, conn) {
  const graph = Array.from({ length: n + 1 }, () => []);
  for (let [a, b] of conn) {
    graph[b].push(a);
  }
  const visited = Array(n + 1);
  
  const bfs = (com) => {
    const stack = [com];
    visited[com] = 1;
    let cnt = 1;

    while (stack.length) {
      const now = stack.pop();
      for (let i = 0; i < graph[now].length; i++) {
        if (!visited[graph[now][i]]) {
          stack.push(graph[now][i]);
          visited[graph[now][i]] = 1;
          cnt++;
        }
      }
    }
    if (maxCnt < cnt) {
      maxCnt = cnt;
      result = [com];
    } else if (maxCnt === cnt) {
      result.push(com);
    }
  }

  let maxCnt = 0;
  let result = [];
  for (let i = 1; i <= n; i++) {
    visited.fill(0);
    bfs(i);
  }
  return result.join(' ');
}

// -------------
// 출력
// -------------
const result = solution1(N, M, CONN);
console.log(result);