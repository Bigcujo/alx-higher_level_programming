#!/usr/bin/node
class Rectangle {
    constructor(w, h){
            if ( typeof w === 'number' && w > 0 && typeof h === 'number' && h > 0) {
                [this.width, this.height] = [w, h];
            }
        }
    // No need to define a constructor or any methods if it's an empty clas
    print() {
                   for (let c = 0; c < this.height; c++){
                           console.log('X'.repeat(this.width));
                   }
           }

    rotate() { 
    	[this.width, this.height] = [this.height, this.width];
    }
    
    double() { 
	    [this.width, this.height] = [this.width * 2, this.height * 2];
    }

};

module.exports = Rectangle;
