const math = require('./math');

// Ecma 2015 below
// console.log(math.add(1, 2));
// console.log(math.subtract(67, 12));

// Ecma 2015
const {add, subtract} = math;
console.log(add(1, 2));
console.log(subtract(54, 23));
