#!/usr/bin/node
// Consuming the starwars api
const request = require('request')

const movieId = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${movieId}/`;

request(url, (error, response, body) => {
    //Error handling and failure alert
    if (error) {
        console.log('Error:', error);
        return
    }

    if (response.statusCode !== 200) {
        console.log('Retry that fetch!:', response.statusCode)
    }

    //parse the received body; get only the characters field
    const data = JSON.parse(body);
    const characters = data['characters']

    //Get each character name and list it.
    characters.forEach(characterUrl => {
        request(characterUrl, (error, response, body) => {
            if (error) {
                console.log('Error:', error);
                return;
            }
            if (response.statusCode !== 200) {
                console.log("Didn't fetch that!", response.statusCode);
                return;
            }

            const charData = JSON.parse(body)
            console.log(charData.name);
        })
    })
})