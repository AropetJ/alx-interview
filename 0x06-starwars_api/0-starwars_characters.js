#!/usr/bin/node
const request = require('request');
const API_URL = 'https://swapi-api.alx-tools.com/api/';

async function getCharacterNames(movieId) {
    try {
        const response = await request.get(`${API_URL}/films/${movieId}`);
        const characterURL = response.data.characters;
        const characterPromise = characterURL.map(async url => {
            const characterResponse = await request.get(url);
            return characterResponse.data.name;
        });
        const characterName = await Promise.all(characterPromise);
        console.log(characterName.join('\n'));
    }
    catch (error) {
        console.error(error);
    }
}

if (process.argv.length > 2) {
    const movieId = process.argv[2];
    getCharacterNames(movieId);
}
