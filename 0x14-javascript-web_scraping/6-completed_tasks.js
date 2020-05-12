#!/usr/bin/node
/* Task 6 -script that computes the number of tasks completed by user id. */
/*  module request */
const request = require('request');
/* The first argument is the API URL: https://jsonplaceholder.typicode.com/todos */
request(process.argv[2], function (error, response, body) {
  if (error) throw error;
  /* computes the number of tasks completed by user id */
  const users = {};
  for (const task of JSON.parse(body)) {
    if (task.completed) {
      if (users[task.userId]) {
        users[task.userId]++;
      } else {
        users[task.userId] = 1;
      }
    }
  }
  console.log(users);
});
