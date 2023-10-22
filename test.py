#!/usr/bin/python3
from flask import Flask, jsonify

app = Flask(__name__)

# Sample data as a Python dictionary
sample_data = {
    "name": "John Doe",
    "email": "john@example.com",
    "age": 30
}

@app.route('/test_jsonify')
def test_jsonify():
    # Use jsonify to convert the Python dictionary to a JSON response
    return jsonify(sample_data)

if __name__ == '__main__':
    app.run(debug=True)

