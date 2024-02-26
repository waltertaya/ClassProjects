const laptops = require('./laptop');
console.log(laptops.getName());
laptops.setName('ASUS');
console.log(laptops.getName());


const newLaptops = require('./laptop');
console.log(newLaptops.getName()); 
// The concept of module caching occurs in such situation where the new instance created is not loaded again from the file once loaded above i.e (remembered).
// The output of the above code will be: 
// HP Pavilion 15
// ASUS
// ASUS