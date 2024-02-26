const add = (a, b) => {
    return a + b;
};

const subtract = (a, b) => {
    return a - b;
};

// In Ecma 2015. Iff key has same name as value
module.exports = {
    add,
    subtract
};

// Bellow 2015
// module.exports = {
//     add: add,
//     subtract: subtract
// }