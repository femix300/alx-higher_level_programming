#!/usr/bin/node
const request = require('request');

request('https://jsonplaceholder.typicode.com/users', (error, response) => {
  if (error) {
    console.log(error);
  }
  console.log('code:', response.statusCode);
});
