#!/usr/bin/node

// Import fs module
const fs = require('fs');

const fileA = fs.readFileSync(process.argv[2]).toString();
const fileB = fs.readFileSync(process.argv[3]).toString();
const concatenatedContent = fileA + fileB;
fs.writeFileSync(process.argv[4], concatenatedContent);
