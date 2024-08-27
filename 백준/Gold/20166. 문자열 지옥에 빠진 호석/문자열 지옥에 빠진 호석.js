const fs = require('fs');
const stdin = fs.readFileSync('/dev/stdin').toString().trim();

// -------------
// 입력
// -------------
const input = stdin.split('\n').map(item => item.trim());
const [N, M, K] = input[0].split(' ').map(Number);
const BOARD = input.slice(1, N + 1);
const STR = input.slice(N + 1);

// -------------
// 풀이 (DFS)
// -------------
function solution(n, m, k, board, strArr) {
  const strCountMap = new Map();
  for (const str of strArr) {
    strCountMap.set(str, 0);
  }
  
  const findWay = (y, x, way) => {
    const X = [1, 1, 0, -1, -1, -1, 0, 1];
    const Y = [0, 1, 1, 1, 0, -1, -1, -1];

    let [nextY, nextX] = [y + Y[way], x + X[way]];
    if (nextY < 0) nextY = n - 1;
    if (nextY >= n) nextY = 0;
    if (nextX < 0) nextX = m - 1;
    if (nextX >= m) nextX = 0;

    return [nextY, nextX];
  }

  const dfs = (y, x, str) => {
    if (str.length > 5)
      return;

    if (strCountMap.has(str)) {
      strCountMap.set(str, (strCountMap.get(str) || 0) + 1);
    }

    for (let i = 0; i < 8; i++) {
      const [nextY, nextX] = findWay(y, x, i);
      dfs(nextY, nextX, str + board[nextY][nextX]);
    }
  }

  for (let r = 0; r < n; r++) {
    for (let c = 0; c < m; c++) {
      dfs(r, c, board[r][c]);
    }
  }

  const result = [];
  for (const str of strArr) {
    result.push(strCountMap.get(str));
  }
  return result.join('\n');
  // return [...strCountMap.values()].join('\n');
}

// -------------
// 출력
// -------------
const result = solution(N, M, K, BOARD, STR);
console.log(result);