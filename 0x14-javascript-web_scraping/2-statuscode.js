#!/usr/bin/node
const request = require('request');

// Get the URL to request from the command line argument
const url = process.argv[2];

// check id URL is provided
if (!url) {
  console.error('please provide URL');
  process.exit(1);
}

// <ake a GEt request to the URL
request.get(url, (error, response) => {
  if (error) {
    console.error(error);
    return;
  }
  // print the status code
  console.log('code:', response.statusCode);
});
