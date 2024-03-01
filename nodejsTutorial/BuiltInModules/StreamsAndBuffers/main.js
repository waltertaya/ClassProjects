const buffer = new Buffer.from('WalterMitty');

console.log(buffer.toString());
console.log(buffer);
console.log(buffer.toJSON());

buffer.write('WalterTaya');

console.log(buffer.toString());
console.log(buffer);
console.log(buffer.toJSON());
