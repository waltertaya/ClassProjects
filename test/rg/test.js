// Get user input using template literals and a multi-line string
const num1 = parseInt(prompt(`Enter the first number:`));
const num2 = parseInt(prompt(`Enter the second number:`));

// Perform calculations
const sum = num1 + num2;
const difference = num1 - num2;
const product = num1 * num2;
const quotient = num1 / num2;
const remainder = num1 % num2;
const exponent = Math.pow(num1, num2);

// Display results using a template literal and concise arrow function
const displayResult = (operation, result) => console.log(`${operation}:`, result);

displayResult("Sum", sum);
displayResult("Difference", difference);
displayResult("Product", product);
displayResult("Quotient", quotient);
displayResult("Remainder", remainder);
displayResult("Exponent", exponent);
