#!/usr/bin/node

let noOfCalls = 0;

exports.logMe = function (item) {
  console.log(noOfCalls + ': ' + item);
  noOfCalls++;
};
