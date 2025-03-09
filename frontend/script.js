const API_BASE_URL = 'http://localhost:5001/api';

const searchInput = document.getElementById('search-input');
const searchButton = document.getElementById('search-button');
const resultsDiv = document.getElementById('results');

searchButton.addEventListener('click', performSearch);

async function performSearch() {
    const query = searchInput.value.trim();
    if (query === '') return;

    resultsDiv.innerHTML = 'Loading...';

    try {
        const cities = await fetchResults('cities', query);
        const countries = await fetchResults('countries', query);
        displayResults(cities, countries);
    } catch (error) {
        console.error('Error searching:', error);
        resultsDiv.innerHTML = 'An error occurred. Please try again.';
    }
}

async function fetchResults(type, query) {
    const response = await fetch(`${API_BASE_URL}/${type}?query=${query}`);
    if (!response.ok) {
        throw new Error('Network response was not ok');
    }
    return await response.json();
}

function displayResults(cities, countries) {
    resultsDiv.innerHTML = '';

    if (cities.length === 0 && countries.length === 0) {
        resultsDiv.innerHTML = 'No results found.';
        return;
    }

    if (cities.length > 0) {
        resultsDiv.innerHTML += '<h2>Cities</h2>';
        cities.forEach(city => {
            resultsDiv.innerHTML += `<p>${city.name}, ${city.country}</p>`;
        });
    }

    if (countries.length > 0) {
        resultsDiv.innerHTML += '<h2>Countries</h2>';
        countries.forEach(country => {
            resultsDiv.innerHTML += `<p>${country}</p>`;
        });
    }
} 