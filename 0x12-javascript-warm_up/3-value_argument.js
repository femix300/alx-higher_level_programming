#!/usr/bin/node

const argPassed = process.argv[2];

if (!argPassed) {
  console.log('No argument');
} else {
  console.log(argPassed);
}
