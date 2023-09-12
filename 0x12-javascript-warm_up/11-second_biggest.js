#!/usr/bin/node

let max = 0;
let sec = 0;

if (process.argv.length <= 3) {
  console.log('0');
} else {
  for (let i = 2; i < process.argv.length; i++) {
    const curr = parseInt(process.argv[i], 10);
    if (!(isNaN(curr))) {
      if (curr > max) {
        sec = max;
        max = curr;
      } else if (curr > sec && curr !== max) {
        sec = curr;
      }
    }
  }
  console.log(sec);
}
