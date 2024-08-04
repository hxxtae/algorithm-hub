const fs = require('fs');
const stdin = fs.readFileSync('/dev/stdin').toString().trim();

// -------------
// 입력
// -------------
const input = stdin.split('\n').map(item => item.trim());
const N = +input[0];
const ENERGE = input.slice(1, N + 1).map(Number);
const ROOMS = input.slice(N + 1).map(list => list.split(' ').map(Number));

// -------------
// 풀이 (DFS)
// -------------
function solution(n, energe, rooms) {
  const table = Array.from({ length: 16 }, () => Array.from({ length: n + 1 }, () => ({})));
  const resultArr = Array(n).fill(1);
  const visited = Array(n + 1).fill(0);
  const graph = Array.from({ length: n + 1 }, () => []);
  for (const [a, b, val] of rooms) {
    graph[a].push([b, val]);
    graph[b].push([a, val]);
  }
  
  const dfs = (node) => {
    for (const [next, val] of graph[node]) {
      if (!visited[next]) {
        visited[next] = 1;
        table[0][next] = { parent: node, total: val };
        dfs(next);
      }
    }
  }

  visited[1] = 1;
  table[0][1] = { parent: 1, total: 0 }
  dfs(1);

  for (let i = 1; i <= 15; i++) {
    for (let node = 1; node <= n; node++) {
      table[i][node].parent = table[i - 1][table[i - 1][node].parent].parent;
      table[i][node].total = table[i - 1][table[i - 1][node].parent].total + table[i - 1][node].total;
    }
  }
  
  const onMoveRoom = (room) => {
    let target = room;
    for (let i = 15; i >= 0; i--) {
      if (table[i][target].parent !== 0 && table[i][target].total <= energe[room - 1]) {
        energe[room - 1] -= table[i][target].total;
        target = table[i][target].parent;
        if (target === 1) return target;
      }
    }

    return target;
  }

  for (let node = 1; node <= n; node++) {
    const arriveRoom = onMoveRoom(node);
    resultArr[node - 1] = arriveRoom;
  }
  
  return resultArr.join('\n');
}

// -------------
// 출력
// -------------
const result = solution(N, ENERGE, ROOMS);
console.log(result);