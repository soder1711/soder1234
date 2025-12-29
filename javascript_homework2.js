// assignment 4
numbers1 = []
while (true) {
    let i = prompt("enter a number")
    let a = parseInt(i);
    if (a !== 0) {
        numbers1.push(a);
    }
    if (a === 0) {
        break
    }
}
numbers1.sort((a, b) => a - b)
numbers1.reverse()
for (let a of numbers1) {
    console.log(a)
}



// assignment 5
const numbers = []
while (true) {
    const input = prompt("enter a number")
    const number = parseInt(input)
    if (numbers.includes(number)) {
        break
    }
    numbers.push(number)
}
numbers.sort((a, b) => a - b)
console.log(numbers)

