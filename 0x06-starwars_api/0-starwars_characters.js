#!/usr/bin/node
// Consuming the starwars api
const starwars = () => {
    return new Promise((resolve, reject) => {
        const request = require('request');

        const movieId = process.argv[2];
        const url = `https://swapi-api.alx-tools.com/api/films/${movieId}/`;

        request(url, (error, response, body) => {
        if(response.statusCode !== 200){
            reject(error)
        }
        const data = JSON.parse(body);
        const CharUrls = data.characters;
        const charPromise = CharUrls.map(char => {
            return new Promise((resolve, reject) => {
                request(char, (error, response, body) => {
                    if (error){
                        reject(error);
                    } else {
                        const charData = JSON.parse(body);
                        resolve(charData.name);
                    }
                });
            });
        });
        Promise.all(charPromise)
            .then(characters => resolve(characters))
            .catch(error => reject(error));
        });
    });
};
starwars().then(characters => {
    characters.forEach(character => {
        console.log(character);
    });
}).catch(error => {
    console.log(error);
});
/*
-> Using callbacks to display received response
starwars((err, data) => {
    console.log('Callback Fired')
    if (err){
        console.log(err)
    } else {
        console.log(data.characters)
    }
});
*/