#!/usr/bin/node
function addMeMaybe(x, callback) {
	const result = x + 1;
	callback(result);
}
module.exports = { addMeMaybe };
