#!/usr/bin/node
const request = require('request')
const movieId = process.argv[2]
const API_URL = `https://swapi.dev/api/films/${movieId}/`

request(API_URL, (error, response, body) => {
  if (error || response.statusCode !== 200) {
    console.error('Error:', error || `Invalid status code: ${response.statusCode}`)
    return
  }
  const charactersURL = JSON.parse(body).characters
  Promise.all(charactersURL.map(url => new Promise((resolve, reject) =>
    request(url, (error, _, body) =>
      error ? reject(error) : resolve(JSON.parse(body).name)
    )
  )))
    .then(names => console.log(names.join('\n')))
    .catch(error => console.error(error))
})
