#!/usr/bin/node
const request = require('request');

const url = process.argv[2];
const targetUrl = 'https://swapi-api.alx-tools.com/api/people/18/';
let count = 0;

request(url, (error, response, body) => {
  if (error) {
    console.log(error);
  }
  const jsonResponse = JSON.parse(body);
  for (let i = 0; i < jsonResponse.results.length; i++) {
    if (jsonResponse.results[i].characters.includes(targetUrl)) {
      count++;
    }
  }
  console.log(count);
});
