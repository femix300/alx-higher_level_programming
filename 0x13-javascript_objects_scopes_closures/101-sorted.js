#!/usr/bin/node
const data = require('./101-data.js');

const dict = data.dict;

const newDict = {};

for (const key in dict) {
  const value = dict[key];

  if (!Object.prototype.hasOwnProperty.call(newDict, value)) {
    newDict[value] = [];
  }

  newDict[value].push(key);
}

console.log(newDict);
