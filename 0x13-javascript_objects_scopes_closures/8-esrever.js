#!/usr/bin/node
exports.esrever = function (list){
	let reversedList = [];
	for ( let f = list.length - 1; f >= 0; f--) {
		reversedList.push(list[f]);
	}
	return reversedList;
}
