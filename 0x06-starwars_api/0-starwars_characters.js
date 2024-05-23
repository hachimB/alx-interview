#!/usr/bin/node
// const request = require('request');
// const util = require('util');

// const requestPromise = util.promisify(request);

// async function getCharacterNames(url) {
//   try {
//     const response = await requestPromise(url);
//     const characters = JSON.parse(response.body).characters;

//     const characterPromises = characters.map(URL => requestPromise(URL));
//     const characterResponses = await Promise.all(characterPromises);

//     characterResponses.forEach(characterResponse => {
//       console.log(JSON.parse(characterResponse.body).name);
//     });
//   } catch (error) {
//     console.log(error);
//   }
// }

// const url = 'https://swapi-api.alx-tools.com/api/films/' + process.argv[2];
// getCharacterNames(url);
const request = require('request');
const util = require('util');

const requestPromise = util.promisify(request);

async function getCharacterNames (url) {
  try {
    const response = await requestPromise(url);
    const characters = JSON.parse(response.body).characters;

    for (const URL of characters) {
      const characterResponse = await requestPromise(URL);
      console.log(JSON.parse(characterResponse.body).name);
    }
  } catch (error) {
    console.log(error);
  }
}

const url = 'https://swapi-api.alx-tools.com/api/films/' + process.argv[2];
getCharacterNames(url);
