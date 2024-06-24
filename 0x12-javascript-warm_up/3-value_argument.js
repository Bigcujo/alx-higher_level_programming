#!/usr/bin/node
const args = process.argv.slice(2);
const argsCount = args.length;
if ( argsCount < 1 ){
    console.log('No argument');
} else if ( argsCount >= 1) {
    console.log(args[0]);
}
