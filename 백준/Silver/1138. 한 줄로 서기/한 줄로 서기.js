const fs = require('fs')
const input = fs.readFileSync('/dev/stdin').toString().trim().split('\n')

const n = +input[0]
const a = input[1].split(' ').map(Number)
const r = []
for (let i = n - 1; i >= 0; i--) r.splice(a[i], 0, i + 1)

console.log(r.join(' '))