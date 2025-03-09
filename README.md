# Simple City Search API

A simple application that allows users to search for cities and countries around the world. The project consists of a frontend interface and a backend API with a city database.

## Project Structure

```
Simple-API-Example/
├── backend/
│   ├── app.py             # Flask API server
│   ├── database.py        # Database connection and models
│   ├── cities.json        # Sample city data
│   └── requirements.txt   # Python dependencies
├── frontend/
│   ├── index.html         # Main HTML page
│   ├── styles.css         # CSS styles
│   └── script.js          # Frontend JavaScript
└── README.md              # Project documentation
```

## Features

- Search for cities and countries by name
- Get city details including country and population
- Simple and responsive UI
- RESTful API backend

## Technologies Used

- **Frontend**: HTML, CSS, JavaScript
- **Backend**: Python, Flask
- **Database**: SQLite (with sample data)

## Getting Started

### Backend Setup

1. Navigate to the backend directory:
   ```
   cd backend
   ```

2. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Start the server:
   ```
   python app.py
   ```

### Frontend Setup

Simply open `frontend/index.html` in your web browser.

## API Endpoints

- `GET /api/cities?query=<search_term>` - Search for cities by name
- `GET /api/countries?query=<search_term>` - Search for countries by name

## License

MIT

## File Descriptions

- **`cities.json`**: Contains sample city data used to populate the database initially.
- **`database.py`**: Manages database connections and operations, including data retrieval for cities and countries.
- **`cities.db`**: SQLite database file storing city and country data.
- **`app.py`**: Flask application that serves the API endpoints for searching cities and countries.
