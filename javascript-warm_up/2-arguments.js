#/usr/bim/node
const args = process.argv.length - 2;

if (args == 0) {
	console.log('No argument');
}else (args == 1) {
	console.log('Argument found');
} else {
	console.log('Arguments found');
}

