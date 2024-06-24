#!/usr/bin/node
const sizeOf = process.argv[2];
if (isNaN(sizeOf)){
    console.log('Missing size');
} else { 
    for (let i = 0; i < sizeOf; i++){
        console.log('X'.repeat(sizeOf))
    }
} 
