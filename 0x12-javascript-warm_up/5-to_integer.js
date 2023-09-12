#!/usr/bin/node

if (isNaN(parseInt(process.argv[2], 10))) {
  console.log('Not a number');
} else {
  const result = parseInt(process.argv[2], 10);
  console.log('My number: ' + result);
}
