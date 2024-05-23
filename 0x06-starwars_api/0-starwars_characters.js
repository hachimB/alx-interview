#!/usr/bin/node
const request = require('request');
const util = require('util');

const requestPromise = util.promisify(request);

async function getCharacterNames (url) {
  try {
    const response = await requestPromise(url);
    const characters = JSON.parse(response.body).characters;

    for (const URL of characters) {
      const characterResponse = await requestPromise(URL);
      const names = JSON.parse(characterResponse.body).name;
      console.log(names);
    }
  } catch (error) {
    console.log(error);
  }
}

const url = 'https://swapi-api.alx-tools.com/api/films/' + process.argv[2];
getCharacterNames(url);
