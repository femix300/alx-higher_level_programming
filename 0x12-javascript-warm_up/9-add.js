#!/usr/bin/node

// A function that adds integers and prints out the result

let a = parseInt(process.argv[2], 10);
let b = parseInt(process.argv[3], 10);

function add(a, b) {
    console.log(a + b);
}

add(a, b);