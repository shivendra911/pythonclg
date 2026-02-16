from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/api/data")
def data():
    return jsonify({
        "message": "Hello from second_app",
        "status": "success"
    })

if __name__ == "__main__":
    app.run(port=9999, debug=True)
