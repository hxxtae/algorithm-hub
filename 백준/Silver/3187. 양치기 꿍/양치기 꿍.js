const fs = require('fs');
const stdin = fs.readFileSync('/dev/stdin').toString().trim();

// -------------
// 입력
// -------------
const input = stdin.split('\n').map(item => item.trim());
const [RC, ...FIELD] = input;
const [R, C] = RC.split(' ').map(Number);

// -------------
// 풀이 (DFS)
// -------------
function solution1(r, c, field) {
  const visited = Array.from({ length: r }, () => Array(c).fill(0));

  const findWay = (y, x, way) => {
    const X = [1, 0, -1, 0];
    const Y = [0, 1, 0, -1];

    return [y + Y[way], x + X[way]];
  }

  const dfs = (y, x, sheep, wolf) => {
    if (field[y][x] === 'k') sheep += 1;
    if (field[y][x] === 'v') wolf += 1;

    for (let i = 0; i < 4; i++) {
      const [nextY, nextX] = findWay(y, x, i);
      if (nextY >= 0 && nextX >= 0 && nextY < r && nextX < c) {
        if (field[nextY][nextX] !== '#' && !visited[nextY][nextX]) {
          visited[nextY][nextX] = 1;
          [sheep, wolf] = dfs(nextY, nextX, sheep, wolf);
        }
      }
    }

    return [sheep, wolf];
  }

  let result = [0, 0];
  for (let row = 0; row < r; row++) {
    for (let col = 0; col < c; col++) {
      if (field[row][col] !== '#' && !visited[row][col]) {
        visited[row][col] = 1;
        const [sheep, wolf] = dfs(row, col, 0, 0);
        if (sheep > wolf) result[0] += sheep;
        else result[1] += wolf;
      }
    }
  }

  return result.join(' ');
}

// -------------
// 출력
// -------------
const result1 = solution1(R, C, FIELD);
console.log(result1);