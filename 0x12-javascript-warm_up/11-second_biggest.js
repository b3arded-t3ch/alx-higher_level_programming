#!/usr/bin/node
const args = process.argv
if ((args.length < 3) || (args.length === 3)) {
	console.log("0");
} else {
	const new_args = args.slice(2);
	for (let i = 0; i < new_args.length; i++) {
		new_args[i] = Number(new_args[i]);
	}
	new_args.sort(function(a, b) {
		return (b - a);
	});
	console.log(new_args[1]);
}
