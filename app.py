from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route('/ping', methods=['GET'])
def ping():
    """Simple health check endpoint."""
    return jsonify({"message": "pong"}), 200


@app.route('/data', methods=['GET'])
def get_data():
    """Returns a JSON object with sample data."""
    sample_data = {"data": "This is a sample response"}
    return jsonify(sample_data), 200


@app.route('/data', methods=['POST'])
def post_data():
    """Receives JSON data and returns it in a response."""
    if not request.is_json:
        return jsonify({"error": "Request must be JSON"}), 400
    data = request.get_json()
    # You can process the data here
    return jsonify({"received": data}), 201


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
