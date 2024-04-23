#!/usr/bin/node
const request = require('request');

// Get the API URL from the command line arguments
const apiUrl = process.argv[2];

// Check if API URL is provided
if (!apiUrl) {
  console.error('Please provide the API URL as an argument.');
  process.exit(1);
}

// Make a GET request to the API URL
request.get(apiUrl, (error, response, body) => {
  if (error) {
    console.error('Error:', error);
    return;
  }

  // Parse the JSON response body
  const todos = JSON.parse(body);

  // Initialize an object to store the count of completed tasks for each user ID
  const completedTasksByUser = {};

  // Iterate through the todos and count completed tasks for each user
  todos.forEach(todo => {
    if (todo.completed) {
      if (!completedTasksByUser[todo.userId]) {
        completedTasksByUser[todo.userId] = 1;
      } else {
        completedTasksByUser[todo.userId]++;
      }
    }
  });

  // Print the count of completed tasks for each user ID
  console.log(completedTasksByUser);
});
