const input = require("fs").readFileSync("/dev/stdin").toString().trim().split("\n");
let idx = 0;

while (idx < input.length - 1) {
  const [N, M] = input[idx++].split(" ").map(Number);
  let onePointer = idx;
  let twoPointer = idx + N;
  let answer = 0;
  while (onePointer < N + idx && twoPointer < N + M + idx) {
    if (Number(input[onePointer]) < Number(input[twoPointer])) {
      onePointer++;
      continue;
    }
    if (Number(input[onePointer]) > Number(input[twoPointer])) {
      twoPointer++;
      continue;
    }
    answer++;
    onePointer++;
    twoPointer++;
  }
  console.log(answer);
  idx += N + M;
}