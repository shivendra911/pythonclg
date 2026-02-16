from flask import Flask, jsonify
import requests

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <h2>First App (5001)</h2>
    <a href="/get-data">Get data from second_app</a>
    """

@app.route("/get-data")
def get_data():
    # SERVER → SERVER call
    response = requests.get("http://127.0.0.1:9991/data")

    # forward response to browser
    return jsonify(response.json())

if __name__ == "__main__":
    app.run(port=5001, debug=True)
