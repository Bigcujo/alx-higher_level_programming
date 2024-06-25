#!/usr/bin/node
 const cmdArgs = process.argv.slice(2);
 if (cmdArgs[0] === undefined) {
    console.log('0');
 } else if (cmdArgs[1] === undefined) {
    console.log('0');
 } else {
    cmdArgs.sort((x, y) => x - y);
    console.log(cmdArgs[cmdArgs.length - 2]); 
}
