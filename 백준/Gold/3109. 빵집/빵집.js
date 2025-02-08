const fs = require('fs');
const stdin = fs.readFileSync('/dev/stdin').toString().trim();

// -------------
// 입력
// -------------
const input = stdin.split('\n').map(item => item.trim());
const [R, C] = input[0].split(' ').map(Number);
const PIPELINE = input.slice(1);

// -------------
// 풀이 (DFS)
// -------------
function solution1(r, c, pipeline) {
  const visited = Array.from({ length: r }, () => Array(c).fill(0));
  const findPipeWay = (y, x, way) => {
    const X = [1, 1, 1];
    const Y = [-1, 0, 1];
    return [y + Y[way], x + X[way]];
  }
  let cnt = 0;

  const dfs = (y, x, arrive) => {
    if (x === c - 1) {
      cnt++;
      return arrive = true;
    }
    for (let i = 0; i < 3; i++) {
      const [nextY, nextX] = findPipeWay(y, x, i);
      if (nextY >= 0 && nextX >= 0 && nextY < r && nextX < c) {
        if (pipeline[nextY][nextX] !== 'x' && !visited[nextY][nextX]) {
          visited[nextY][nextX] = 1;
          arrive = dfs(nextY, nextX);
          if (arrive) return true;
        }
      }
    }
  }

  for (let i = 0; i < r; i++) {
    if (pipeline[i][0] !== 'x') {
      visited[i][0] = 1;
      dfs(i, 0, false);
    }
  }
  return cnt;
}

// -------------
// 출력
// -------------
const result1 = solution1(R, C, PIPELINE);
console.log(result1);
