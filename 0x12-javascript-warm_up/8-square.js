#!/usr/bin/node
const arg = process.argv[2]
for (let i = 0; i < arg; i++) {
	for (let j = 0; j < arg; j++) {
		process.stdout.write("x");
	}
	console.log();
}
