#!/usr/bin/node
const args = process.argv.slice(2);
const argsCount = args.length;
if ( args < 1 ){
    console.log('No argument');
} else {
    console.log('Arguments found');
}
