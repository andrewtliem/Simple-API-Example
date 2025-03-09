from flask import Flask, jsonify, request, send_from_directory
from flask_cors import CORS
import database
import os

app = Flask(__name__, static_folder='../frontend', static_url_path='/')
CORS(app)

database.init_db()

@app.route('/api/cities', methods=['GET'])
def get_cities():
    search_query = request.args.get('query', '')
    cities = database.get_cities(search_query)
    return jsonify(cities)

@app.route('/api/countries', methods=['GET'])
def get_countries():
    search_query = request.args.get('query', '')
    countries = database.get_countries(search_query)
    return jsonify(countries)

@app.route('/')
def serve_index():
    return send_from_directory('../frontend', 'index.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5001) 