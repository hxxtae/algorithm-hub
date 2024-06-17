const fs = require('fs');
const input = fs.readFileSync('/dev/stdin').toString().trim();
const regexpTag = /(\<[a-z\s]+\>)/g;
const regexpText = /([a-z0-9\s]+)/g;

function solution(str) {
  const resultArr = [];
  const tagArr = str.match(regexpTag);

  let strArr = str.replace(regexpTag, '.<TAG>.').replace(regexpText, '.<STR>.');
  strArr = strArr.split('.').filter(value => value ? true : false);  

  let textArr = str.replace(regexpTag, '<TAG>').split('<TAG>').filter(item => 
    item ? true : false
  );
  textArr = textArr.map(item => item
    .split(' ')
    .map(text => text.split('').reverse().join(''))
    .join(' '));
  
  if (tagArr === null) {
    console.log(textArr.join(''));
  } else {
    let tagIdx = 0;
    let textIdx = 0;
    strArr.map(value => {
      if (value === '<TAG>') {
        resultArr.push(tagArr[tagIdx++]);
      } else if (value === '<STR>') {
        resultArr.push(textArr[textIdx++]);
      }
    });
    console.log(resultArr.join(''));
  }
}

solution(input);