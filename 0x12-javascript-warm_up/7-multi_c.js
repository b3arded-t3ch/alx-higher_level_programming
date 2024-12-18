#!/usr/bin/node
const arg = process.argv[2]
let count = 0;
if (!isNaN(arg)) {
	while (count < arg) {
		count++;
		console.log("C is fun")
	}
} else {
	console.log("Missing number of occurrences")
}
