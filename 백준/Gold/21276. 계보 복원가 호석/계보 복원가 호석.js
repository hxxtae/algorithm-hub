const fs = require('fs');
const stdin = fs.readFileSync('/dev/stdin').toString().trim();

// -------------
// 입력
// -------------
const [N, CITIZEN, M, ...XYARR] = stdin.split('\n').map(item => item.trim());

// -------------
// 풀이
// -------------
function solution(n, citizen, m, xyArr) {
  citizen = citizen.split(' ');
  xyArr = xyArr.map(xy => xy.split(' '))
  const linkMap = new Map(citizen.map(name => [name, []])); // A(parent) 노드에서 B(child) 노드로 진입하는 경로
  const inDegree = new Map(citizen.map(name => [name, 0])); // B(child) 노드에 진입할 수 있는 경로의 개수
  const queue = [];
  const trees = new Map();
  const roots = [];

  for (const [child, parent] of xyArr) {
    linkMap.get(parent).push(child);
    inDegree.set(child, inDegree.get(child) + 1);
  }

  for (const root of citizen) {
    if (inDegree.get(root) === 0) {
      queue.push(root);
      roots.push(root);
    }
  }

  while (queue.length) {
    const node = queue.shift();
    trees.set(node, []);

    for (let i = 0; i < linkMap.get(node).length; i++) {
      const child = linkMap.get(node)[i];
      
      inDegree.set(child, inDegree.get(child) - 1); // 진입 경로 개수 1 제거
      if (inDegree.get(child) === 0) { // 진입 경로 개수가 0
        trees.get(node).push(child);
        queue.push(child)
      }
    }
  }
  const rootLen = roots.length.toString();
  const rootNames = roots.sort().join(' ');
  const treeNames = [...trees.keys()].sort().map(parent =>
    `${parent} ${trees.get(parent).length} ${trees.get(parent).sort().join(' ')}`.trim()).join('\n');
  console.log(rootLen)
  console.log(rootNames)
  console.log(treeNames)
}

// -------------
// 출력
// -------------
solution(N, CITIZEN, M, XYARR);


