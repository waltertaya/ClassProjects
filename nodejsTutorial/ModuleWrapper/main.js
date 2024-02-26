(function() {
    console.log("This is a laptop from Asus");
});
// Before the module is executed, it is wrapped in a function expression with 5 parameters namely __dirname, __filename, exports, module, require
// The module is then executed and the function is called with the parameters passed to it
// The module is then returned to the require function