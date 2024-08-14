const fs = require('fs');
const stdin = fs.readFileSync('/dev/stdin').toString().trim();

// -------------
// 입력
// -------------
const input = stdin.split('\n').map(item => item.trim().split(' ').map(Number));
const [[N, M], ...SEA] = input;

// -------------
// 풀이 (DFS)
// -------------
function solution1(n, m, sea) {
  // visited Year (빙하 변화 년도)
  const visited = Array.from({ length: n }, () => Array(m).fill(0));

  const findWay = (y, x, way) => {
    const X = [1, 0, -1, 0];
    const Y = [0, 1, 0, -1];
    return [y + Y[way], x + X[way]];
  }

  const dfs = (nowY, nowX, year) => {
    for (let i = 0; i < 4; i++) {
      const [nextY, nextX] = findWay(nowY, nowX, i);
      if (nextY >= 0 && nextX >= 0 && nextY < n && nextX < m) {
        if (visited[nextY][nextX] !== year) {
          
          if (sea[nextY][nextX]) {
            visited[nextY][nextX] = year;
            dfs(nextY, nextX, year);
          } else {
            !sea[nowY][nowX] || sea[nowY][nowX]--;
          }

        }
      }
    }
  }

  
  let count = 0;
  let year = 0;
  while (count < 2) {
    count = 0;
    year++;
    for (let r = 0; r < n; r++) {
      for (let c = 0; c < m; c++) {
        if (sea[r][c] && visited[r][c] !== year) {
          count++;
          visited[r][c] = year;
          dfs(r, c, year);
        }
      }
    }
    if (count === 0) break;
  }
  return count > 1 ? year-1 : 0;
}

// -------------
// 출력
// -------------
const result1 = solution1(N, M, SEA);
console.log(result1);