#!/usr/bin/node
// Consuming the starwars api
const request = require('request')

const movieId = process.argv[2]
const url = `https://swapi-api.alx-tools.com/api/films/${movieId}/`;

request(url, (error, response, body) => {
    if (error) console.log(error)

    console.log(response.statusCode);
    console.log(body);

    const text = JSON.parse(response);
    console.log(text);

    const characters = test['characters']
    for (const character in characters){
        names = character['name'];
        if (names) {
            console.log(names);
        }
    }
})