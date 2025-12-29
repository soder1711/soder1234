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
for (a of numbers1) {
    console.log(a)
}


while (a !== 0) {
    let i = prompt("enter a number")
    numbers1.push(a)
    a = parseInt(i)
}
if (a === 0) {
    console.log("the loop has ended")
    numbers1.push(a)
}
console.log(numbers1)


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

