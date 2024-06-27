#!/usr/bin/node
exports.nbOccurences = function(list, searchElement) {
	let count = 0;

	for (let f = 0; f < list.length; f++) {
	if (list[f] === searchElement){
	count++;
	}
	}
	return count;
};
