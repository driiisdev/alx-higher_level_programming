#!/usr/bin/node

const list = require('./100-data.js').list;

const newlist = list.map((num, index) => {
  return (num * index);
});

console.log(list);
console.log(newlist);
