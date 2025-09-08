from flask import Flask, jsonify
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

@app.route('/api/message')
def get_message():
    return jsonify({"message": "Hello, Udhayabharathi"})

@app.route('/')
def index():
    return jsonify({
        "message": "Welcome to the API",
        "endpoints": {
            "message": "/api/message"
        }
    })

if __name__ == '__main__':
    print("Starting server on http://localhost:5000")
    print("API endpoint: http://localhost:5000/api/message")
    app.run(debug=True, port=5000)