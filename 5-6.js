// 'use strict';
//
// async function getRandomJoke() {
//     try {
//         const response = await fetch('https://api.chucknorris.io/jokes/random');
//         const data = await response.json();
//         console.log(data.value);
//     }
//     catch (error) {
//         console.log(error.message);
//     }
//     finally {
//         console.log('asynchronous load complete');
//     }
// }
// getRandomJoke();

'use strict';

const form = document.querySelector('form');
const input = document.querySelector('#query');
const results = document.querySelector('#results');

form.addEventListener('submit', async (event) => {
    event.preventDefault();
    const search = input.value;
    try {
        const response = await fetch(
            `https://api.chucknorris.io/jokes/search?query=${search}`
        );

        const data = await response.json();

        console.log(data);

        for (const joke of data.result) {
            const p = document.createElement('p');
            p.textContent = joke.value;
            results.appendChild(p);
        }
    }
    catch (error) {
        console.log(error.message);
    }
});