#!/usr/bin/node

const fs = require('fs');

if (process.argv.length !== 5) {
  console.log('Usage: node concat.js <file1> <file2> <output_file>');
  process.exit(1);
}

const file1 = process.argv[2];
const file2 = process.argv[3];
const outputFile = process.argv[4];

// Read the contents of file1 (if it exists)
const data1 = fs.existsSync(file1) ? fs.readFileSync(file1, 'utf8') : '';
const data2 = fs.readFileSync(file2, 'utf8');

const concatenatedData = (data1 !== '' ? data1 + '\n' : '') + data2;

fs.writeFile(outputFile, concatenatedData, 'utf8', (err) => {
  if (err) {
    process.exit(1);
  }
console.log(concatenatedData);
});
