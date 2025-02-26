#!/usr/bin/node 

const request = require('request');
const url = process.argv[2];

if (!url) {
    console.error('Usage: ./6-completed_tasks.js <URL>');
    process.exit(3);
}

request(url, (error, response, body) => {
    if (error){
        console.error(error);
        return;
    }
    try {
        const todos = JSON.parse(body);
        const completedTasks = {};

        todos.forEach(todo => {
            if (todo.completed) {
                if (!completedTasks[todo.userId]) {
                    completedTasks[todo.userId] = 0;
                }
                completedTasks[todo.userId]++;
            }
        });
        console.log(completedTasks);
    } catch (parseError) {
        console.error('Error parsing JSON:', parseError);
    }

});





