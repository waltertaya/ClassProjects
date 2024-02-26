const Person1 = {
    name: 'Mark',
    age: 21
};

// const Person2 = Person1;
// Person2.name = 'John';   // Work similar to exports only
// console.log(Person1.name); // John

// To overcome the above so that we can have different values for Person1 and Person2, we can use definition literals instead of object literals
const Person2 = {
    name: Person1.name,
    age: Person1.age
};
console.log(Person1.name); // Mark