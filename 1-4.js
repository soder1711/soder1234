// assignment 1-4
'use strict';
const form = document.querySelector('form');
const input = document.querySelector('#query');
const results = document.querySelector('#results');
form.addEventListener('submit', async (event) => {
    event.preventDefault();
    const search = input.value
    try {
        const response = await fetch(`https://api.tvmaze.com/search/shows?q=${search}`)
        const data = await response.json()
        console.log(data)

        for (const tvShow of data) {
            const show = tvShow.show;

            const h2 = document.createElement('h2')
            h2.textContent = show.name;

            const a = document.createElement('a')
            a.href = show.url;
            a.textContent = show.url;
            a.target = '_blank';

            const img = document.createElement('img')
            // if (show.image?.medium) {
            //     img.src = show.image.medium;
            //     img.alt = show.name;
            // }
            // this was replaced due to exercise 4
            img.src = show.image
            ? show.image.medium
                : 'https://placehold.co/210x295?text=Not%20Found'
            img.alt = show.name;

            const summaryDiv = document.createElement('div')
            summaryDiv.innerHTML = show.summary;

            const article = document.createElement('article')
            article.appendChild(h2)
            article.appendChild(a)
            article.appendChild(img)
            article.appendChild(summaryDiv)
            results.appendChild(article)
        }
    }
    catch (error) {
        console.log(error.message);
    }
    finally {
        console.log('asynchronous load complete');
    }
})