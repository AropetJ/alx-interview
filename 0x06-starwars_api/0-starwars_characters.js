#!/usr/bin/node
const request = require('request')
const movieId = process.argv[2]
const API_URL = `https://swapi.dev/api/films/${movieId}/`

request(API_URL, (error, response, body) => {
  if (error) {
    console.error('Error:', error)
    return
  }
  if (response.statusCode !== 200) {
    console.error('Invalid status code:', response.statusCode)
    return
  }
  const film = JSON.parse(body)
  const charactersURL = film.characters
  const getCharacterNamesPromises = charactersURL.map(characterURL => {
    return new Promise((resolve, reject) => {
      request(characterURL, (error, _, characterBody) => {
        if (error) {
          reject(error)
          return
        }
        const character = JSON.parse(characterBody)
        resolve(character.name)
      })
    })
  })
  Promise.all(getCharacterNamesPromises)
    .then(characterNames => console.log(characterNames.join('\n')))
    .catch(error => console.error(error))
})
