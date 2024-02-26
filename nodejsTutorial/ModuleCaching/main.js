// const laptops = require('./laptop');
// console.log(laptops.getName());
// laptops.setName('ASUS');
// console.log(laptops.getName());


// const newLaptops = require('./laptop');
// console.log(newLaptops.getName());
const laptop = require('./laptop')

const asus = new laptop('ASUS');
console.log(asus.getName());
asus.setName('ASUS v2');
console.log(asus.getName());

const hp = new laptop('HP Pavilion 15');
console.log(hp.getName());
hp.setName('HP Pavilion 15 v2');
console.log(hp.getName());
// The concept of module caching occurs in such situation where the new instance created is not loaded again from the file once loaded above i.e (remembered).
// The output of the above code will be: 
// HP Pavilion 15
// ASUS
// ASUS