#!/usr/bin/node
const request = require('request')

const API_URL = 'https://swapi-api.hbtn.io/api'

if (process.argv.length > 2) {
  const movieId = process.argv[2]
  request(`${API_URL}/films/${movieId}/`, (err, _, body) => {
    if (err) {
      console.error(err)
      return
    }

    const movie = JSON.parse(body)
    const characterURL = movie.characters

    const getCharacterNamePromises = characterURL.map(characterURL => {
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

    Promise.all(getCharacterNamePromises)
      .then(characterNames => console.log(characterNames.join('\n')))
      .catch(error => console.error(error))
  })
}
