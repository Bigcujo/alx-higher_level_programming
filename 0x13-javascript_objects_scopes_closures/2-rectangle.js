#!/usr/bin/node
class Rectangle {
    constructor(w, h){
            if ( typeof w === 'number' && w > 0 && typeof h === 'number' && h > 0) {
                [this.width, this.height] = [w, h];
            }
    // No need to define a constructor or any methods if it's an empty class

    }
};
module.exports = Rectangle;
