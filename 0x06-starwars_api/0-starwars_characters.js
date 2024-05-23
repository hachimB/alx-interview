#!/usr/bin/node
const request = require('request');
const url = 'https://swapi-api.alx-tools.com/api/films/' + process.argv[2];
request(url, (error, response, body) => {
  if (error) {
    return console.log(error);
  }
  if (response.statusCode === 200) {
    const characters = JSON.parse(body).characters;
    characters.forEach(URL => {
      request(URL, (error, response, body) => {
        if (error) {
          return console.log(error);
        }
        if (response.statusCode === 200) {
          console.log(JSON.parse(body).name);
        }
      });
    });
  }
});
