// API base URL - change this to match your backend server
const API_BASE_URL = 'http://localhost:5000/api';

// DOM Elements
const searchInput = document.getElementById('search-input');
const searchButton = document.getElementById('search-button');
const resultsList = document.getElementById('results-list');
const cityDetails = document.getElementById('city-details');
const detailContent = document.getElementById('detail-content');
const backButton = document.getElementById('back-button');
const loadingElement = document.getElementById('loading');
const errorMessage = document.getElementById('error-message');

// Event Listeners
searchButton.addEventListener('click', performSearch);
searchInput.addEventListener('keypress', (e) => {
    if (e.key === 'Enter') {
        performSearch();
    }
});
backButton.addEventListener('click', showResultsList);

// Initialize the app
function init() {
    // Focus on search input when page loads
    searchInput.focus();
}

// Perform search
async function performSearch() {
    const query = searchInput.value.trim();
    
    if (query === '') {
        return;
    }
    
    showLoading();
    hideError();
    
    try {
        const cities = await fetchCities(query);
        displayResults(cities);
    } catch (error) {
        console.error('Error searching cities:', error);
        showError();
    } finally {
        hideLoading();
    }
}

// Fetch cities from API
async function fetchCities(query) {
    const response = await fetch(`${API_BASE_URL}/cities?query=${encodeURIComponent(query)}`);
    
    if (!response.ok) {
        throw new Error(`HTTP error! Status: ${response.status}`);
    }
    
    return await response.json();
}

// Display search results
function displayResults(cities) {
    resultsList.innerHTML = '';
    
    if (cities.length === 0) {
        resultsList.innerHTML = '<div class="city-item"><p>No cities found. Try a different search term.</p></div>';
        return;
    }
    
    cities.forEach(city => {
        const cityElement = document.createElement('div');
        cityElement.className = 'city-item';
        cityElement.innerHTML = `
            <h3>${city.name}</h3>
            <p>${city.country}</p>
        `;
        
        cityElement.addEventListener('click', () => {
            showCityDetails(city);
        });
        
        resultsList.appendChild(cityElement);
    });
    
    showResultsList();
}

// Show city details
function showCityDetails(city) {
    detailContent.innerHTML = `
        <div class="detail-card">
            <h2>${city.name}</h2>
            <p class="detail-info"><span>Country:</span> ${city.country}</p>
            <p class="detail-info"><span>Population:</span> ${formatNumber(city.population)}</p>
            <p class="detail-info"><span>Coordinates:</span> ${city.latitude.toFixed(4)}, ${city.longitude.toFixed(4)}</p>
        </div>
    `;
    
    resultsList.classList.add('hidden');
    cityDetails.classList.remove('hidden');
}

// Show results list
function showResultsList() {
    cityDetails.classList.add('hidden');
    resultsList.classList.remove('hidden');
}

// Show loading indicator
function showLoading() {
    loadingElement.classList.remove('hidden');
}

// Hide loading indicator
function hideLoading() {
    loadingElement.classList.add('hidden');
}

// Show error message
function showError() {
    errorMessage.classList.remove('hidden');
}

// Hide error message
function hideError() {
    errorMessage.classList.add('hidden');
}

// Format number with commas
function formatNumber(num) {
    return num.toString().replace(/\B(?=(\d{3})+(?!\d))/g, ',');
}

// Initialize the app when the page loads
document.addEventListener('DOMContentLoaded', init);