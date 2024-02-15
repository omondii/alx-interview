#!/usr/bin/node
// Consuming the starwars api
const request = require('request')

const movieId = process.argv[2]
const url = `https://swapi-api.alx-tools.com/api/films/${movieId}/`;

request(url, (error, response, body) => {
    if (error) {
        console.log('Error:', error);
        return
    }

    console.log(response.statusCode);
    //console.log(body);

    const data = JSON.parse(body);
    console.log(data);

    const characters = data['characters']
    characters.forEach(characterUrl =>{
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