const fs = require('fs');
const stdin = fs.readFileSync('/dev/stdin').toString().trim();

// -------------
// 입력
// -------------
const input = stdin.split('\n').map(item => item.trim());
const [R, C] = input[0].split(' ').map(Number);
const TABLE = input.slice(1);

// -------------
// 풀이
// -------------
function solution(r, c, table) {
    
  const confirmStr = (startRow) => {
    const set = new Set();
    for (let col = 0; col < c; col++) {
      let str = "";
      for (let row = startRow; row < r; row++) {
        str += table[row][col];
      }
      set.add(str);
    }
    // 중복 있음
    if (c !== set.size) return true;
    // 중복 없음
    return false;
  }

  let count = 0;
  let start = 1, end = r - 1;
  while (start <= end) {
    let mid = Math.floor((start + end) / 2);
    const confirm = confirmStr(mid);

    if (confirm) { // 중복 있음
      end = mid - 1;
    } else { // 중복 없음
      start = mid + 1;
      count = mid;
    }
  }

  return count;
}

// -------------
// 출력
// -------------
const result = solution(R, C, TABLE);
console.log(result);
