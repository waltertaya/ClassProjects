// const upperCase = require('upper-case').upperCase;
import { upperCase, localeUpperCase } from "upper-case";


function laptop (name) {
    console.log(upperCase(`You have ${name} laptop. It is recommended laptop for commercial purposes.`));
};

laptop('Asus');
// module.exports = laptop;
