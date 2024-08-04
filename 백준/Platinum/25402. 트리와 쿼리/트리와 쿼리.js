const fs = require('fs');
const stdin = fs.readFileSync('/dev/stdin').toString().trim()

// -------------
// 입력
// -------------
const input = stdin.split('\n').map(item => item.trim());
const [N, TREE, Q, Q_ARR] = [
  +input[0],
  input.slice(1, +input[0]),
  input[+input[0]],
  input.slice(+input[0] + 1)
];

// -------------
// 풀이 (DFS)
// -------------
function solution(n, tree, q, q_arr) {
  const resultArr = [];
  const parents = Array(n + 1).fill(1);
  const visited = Array(n + 1).fill(0);
  const graph = Array.from({ length: n + 1 }, () => []);
  for (const uv of tree) {
    const [u, v] = uv.split(' ').map(Number);
    graph[u].push(v);
    graph[v].push(u);
  }

  const getParent = (node, sParent) => {
    while (node !== sParent[node]) {
      sParent[node] = sParent[sParent[node]];
      node = sParent[node];
    }
    return sParent[node];
  }

  const setParent = (nodeA, nodeB, sParent) => {
    const [a, b] = [getParent(nodeA, sParent), getParent(nodeB, sParent)];
    if (a > b) return sParent[a] = b;
    return sParent[b] = a;
  }

  const findParent = (nodeA, nodeB, sParent) => {
    const [a, b] = [getParent(nodeA, sParent), getParent(nodeB, sParent)];
    if (a === b) return true;
    return false;
  }

  const dfs = (node) => {
    visited[node] = 1;

    for (const next of graph[node]) {
      if (visited[next]) continue;
      visited[next] = 1;
      parents[next] = node;
      dfs(next);
    }
  }

  const bfs = (root) => {
    const queue = [root];
    visited[root] = 1;
    while (queue.length) {
      const node = queue.pop();
      for (const next of graph[node]) {
        if (visited[next]) continue;
        visited[next] = 1;
        queue.push(next);
        parents[next] = node;
      }
    }
  }

  // dfs(1);
  bfs(1);
  let parentOfS = Array.from({ length: n + 1 }, (_, idx) => idx);
  const isinS = Array(n + 1).fill(0);
  
  for (let i = 0; i < q; i++) {
    const [K, ...S] = q_arr[i].split(' ').map(Number);
    for (const node of S) isinS[node] = 1;
    for (let j = 0; j < K; j++) {
      const node = S[j];
      if (isinS[parents[node]]) {
        if (!findParent(node, parents[node], parentOfS)) {
          setParent(node, parents[node], parentOfS);
        }
      }
    }
    for (let node = 1; node <= n; node++) {
      parentOfS[node] = getParent(node, parentOfS);
    }

    const sMap = new Map();
    for (const node of S) {
      sMap.set(parentOfS[node], (sMap.get(parentOfS[node]) || 0) + 1);
    }
    
    console.log([...sMap.values()].reduce((sum, num) => sum + (num * (num - 1)) / 2, 0));

    isinS.fill(0);
    parentOfS = Array.from({ length: n + 1 }, (_, idx) => idx);
  }

}

// -------------
// 출력
// -------------
solution(N, TREE, Q, Q_ARR);