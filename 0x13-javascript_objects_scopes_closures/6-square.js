#!/usr/bin/node
const Basesquare = require('./5-square.js');
class Square extends Basesquare {
	charPrint(c) {
	if (c === undefined) {
		this.print();
	} else {
		for (let f =0; f < this.height; f++) {
			console.log(c.repeat(this.width));
		}
	}
}
};
module.exports = Square;
