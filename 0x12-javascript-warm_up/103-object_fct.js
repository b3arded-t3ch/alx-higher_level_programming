#!/usr/bin/node
const myObject = {
	type: 'object'
	value: 12
};
console.log(myObject);
function myFunc () {
	return ++myObject.value;
};
