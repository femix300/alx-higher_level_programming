#!/usr/bin/node
const data = require('./100-data.js');

const list = data.list;

const newList = list.map((index, element) => index * element);

console.log(list);
console.log(newList);
