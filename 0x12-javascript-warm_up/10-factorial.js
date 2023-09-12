#!/usr/bin/node

// a function that computes the factorial of a given number.

const num = parseInt(process.argv[2], 10);

function factorial (num) {
  if (num <= 1 || isNaN(parseInt(process.argv[2], 10))) { return 1; } else { return num * factorial(num - 1); }
}

console.log(factorial(num));
