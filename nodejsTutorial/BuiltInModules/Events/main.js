// Node.js has a built-in module called Events that allows you to create, fire, and listen for your own events.
const EventEmitter = require("node:events");

// Create an instance of EventEmitter
const emitter = new EventEmitter();

// Listen for the "order-pizza" event
emitter.on("order-pizza", (size, topping) => {
    console.log(`Order received! Baking a ${size} pizza with ${topping}`);
});

// Listen for the "order-pizza" event
emitter.on("order-pizza", (size) => {
    if (size === "large") {
        console.log("Serving complimentary drink!");
    }
});

console.log("Ordering a pizza...");
// Fire/emit the "order-pizza" event
emitter.emit("order-pizza", "large", "pepperoni");
