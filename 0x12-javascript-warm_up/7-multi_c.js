#!/usr/bin/node

if (isNaN(parseInt(process.argv[2], 10))) {
  console.log('Missing number of occurrences');
} else {
  const result = parseInt(process.argv[2], 10);
  for (let i = 0; i < result; i++) {
    console.log('C is fun');
  }
}
