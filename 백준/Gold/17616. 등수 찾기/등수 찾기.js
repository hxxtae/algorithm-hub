const fs = require('fs');
const stdin = fs.readFileSync('/dev/stdin').toString().trim();

// -------------
// 입력
// -------------
const input = stdin.split('\n').map(item => item.trim().split(' ').map(Number));
const [[N, M, X], ...RANK] = input;

// -------------
// 풀이 (DFS)
// -------------
function solution(n, m, x, rank) {
  const visited = Array(n + 1).fill(0);
  const graphA = Array.from({ length: n + 1 }, () => []);
  const graphB = Array.from({ length: n + 1 }, () => []);
  for (const [a, b] of rank) {
    graphA[a].push(b);
    graphB[b].push(a);
  }
  
  const dfsOfWorse = (node, cnt) => {
    for (const next of graphA[node]) {
      if (visited[next]) continue;
      visited[next] = 1;
      cnt = dfsOfWorse(next, cnt + 1);
    }
    
    return cnt;
  }

  const dfsOfBetter = (node, cnt) => {
    for (const next of graphB[node]) {
      if (visited[next]) continue;
      visited[next] = 1;
      cnt = dfsOfBetter(next, cnt + 1);
    }

    return cnt;
  }

  const worseX = dfsOfWorse(x, 0);
  visited.fill(0);
  const betterX = dfsOfBetter(x, 0);
  
  return [1 + betterX, n - worseX].join(' ');
}

// -------------
// 출력
// -------------
const result = solution(N, M, X, RANK);
console.log(result);