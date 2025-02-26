#!/usr/bin/node

const request = require('request');
const fs = require('fs');
const url = process.argv[2];
const file = process.argv[3];

if (!url || !file) {
    console.error('Usage: ./5-request_store.js <URL> <file path>');
    process.exit(2);
}

request(url, (error, response, body) => {
    if (error){
        console.error(error);
        return;
    }
    fs.writeFile(file, body, 'utf-8', (err) => {
        if (err) { 
            console.error(err);
        }
    });
}
);