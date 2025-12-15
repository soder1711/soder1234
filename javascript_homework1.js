// assignment 1
'use strict';
console.log("I am printing to console");


// assignment 2
const name = prompt("Type your name");
console.log('Noice to meet you, ' + name);


// assignment 3
let number1 = prompt("Enter your number");
let number2 = prompt("Enter your number");
let number3 = prompt("Enter your number");
const number4 = parseInt(number1);
const number5 = parseInt(number2);
const number6 = parseInt(number3);
let sum = number4 + number5 + number6;
let product = number4 * number5 * number6;
let average = sum / 3;
console.log(sum);
console.log(average);
console.log(product);


// assignment 4
function getRandomInt(min, max) {
    const minCeiled = Math.ceil(min);
    const maxFloored = Math.floor(max);
    return Math.floor(Math.random() * (maxFloored - minCeiled) + minCeiled);
}
const name1 = prompt("Enter your name");
let house = getRandomInt(1, 5);
if (house === 1) {
    console.log(name1 + ", you are Gryffindor");
}
if (house === 2) {
    console.log(name1 + ", you are Slytherin");
}
if (house === 3) {
    console.log(name1 + ", you are Hufflepuff");
}
if (house === 4) {
    console.log(name1 + ", you are Ravenclaw");
}


// assignment 5
const year1 = prompt("Enter your year");
const year = parseInt(year1);
if (year % 400 ===0) {
    console.log("The year " + year + " is a leap year");
}
else if (year % 100 === 0) {
    console.log("The year " + year + " is not a leap year");
}
else if (year % 4 === 0) {
    console.log("The year " + year + " is a leap year");
}


// assignment 6
const question = confirm("Should I calculate the square root");
if (question === true) {
    let number7 = prompt("Enter a number");
    let number8 = parseInt(number7);
    if (number8 < 0) {
        console.log("The square root of a negative number is not defined");
    }
    if (number8 > 0) {
        console.log(number8 ** 2);
    }
}


// assignment 7
function getRandomInt1(min, max) {
    const minCeiled = Math.ceil(min);
    const maxFloored = Math.floor(max);
    return Math.floor(Math.random() * (maxFloored - minCeiled) + minCeiled);
}
let number9 = prompt("How many dices do you wanna roll?");
const rolls = parseInt(number9);
let sum1 = 0;
for (let i = 0; i < rolls; i++) {
    let dice = getRandomInt1(1, 7);
    sum1 += dice;
}
console.log(sum1);