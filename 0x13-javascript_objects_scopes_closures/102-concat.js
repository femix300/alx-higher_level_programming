#!/usr/bin/node

// Import fs module
const fs = require('fs');

// Destructure the command-line arguments
const [, , fileAPath, fileBPath, fileCPath] = process.argv;

// Read fileA
const fileAContent = fs.readFileSync(fileAPath, 'utf-8');

// Read fileB
const fileBContent = fs.readFileSync(fileBPath, 'utf-8');

// Concatenate fileA and fileB with a new line to separate them
const concatContent = fileAContent + '\n' + fileBContent;

// Write the concatenated contents to fileC
fs.writeFileSync(fileCPath, concatContent, 'utf-8');

console.log(concatContent);
