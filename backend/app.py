from flask import Flask, jsonify, request
from flask_cors import CORS
import database

# Initialize the Flask application
app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# Initialize the database
database.init_db()

@app.route('/api/cities', methods=['GET'])
def get_cities():
    """
    Get cities, optionally filtered by search query
    Example: /api/cities?query=new
    """
    search_query = request.args.get('query', '')
    cities = database.get_cities(search_query)
    return jsonify(cities)

@app.route('/api/cities/<int:city_id>', methods=['GET'])
def get_city(city_id):
    """Get a specific city by ID"""
    city = database.get_city_by_id(city_id)
    if city:
        return jsonify(city)
    return jsonify({"error": "City not found"}), 404

@app.errorhandler(404)
def not_found(error):
    """Handle 404 errors"""
    return jsonify({"error": "Not found"}), 404

@app.errorhandler(500)
def server_error(error):
    """Handle 500 errors"""
    return jsonify({"error": "Server error"}), 500

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)