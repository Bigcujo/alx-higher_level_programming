#!/usr/bin/node

const request = require('request');
const url = process.argv[2];

request(url, (error, response, body ) => {
    if (error){
        console.error(error);
        return;
    } 
    try { 
        const data = JSON.parse(body);

        const count = data.results.filter( movie => 
            movie.characters.some(character => character.includes('/18/'))
            ).length;
        console.log(count);
    } catch (parseError) {
        console.error('Error parsing JSON:', parseError);
    }
    }
);
