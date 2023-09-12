#!/usr/bin/node

let max = 0;
let sec = 0;

if (process.argv.length <= 3) {
  console.log('0');
} else if (process.argv.length === 4) {
  if (process.argv[2] > process.argv[3]) {
    sec = process.argv[3];
  } else {
    sec = process.argv[2];
  }
  console.log(sec);
} else {
  for (let i = 2; i < process.argv.length; i++) {
    const curr = process.argv[i];
    if (curr > max) {
      sec = max;
      max = curr;
    }
  }
  console.log(sec);
}
