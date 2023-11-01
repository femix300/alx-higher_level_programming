#!/usr/bin/node
const request = require('request');
const url = 'https://jsonplaceholder.typicode.com/todos';
request(url, (error, response, body) => {
  if (error) {
    console.log(error);
  }

  const tasks = JSON.parse(body);

  const completedTasks = {};

  for (const task of tasks) {
    if (task.completed) {
      const userId = task.userId;
      if (completedTasks[userId]) {
        completedTasks[userId]++;
      } else {
        completedTasks[userId] = 1;
      }
    }
  }

  console.log(completedTasks);
});
