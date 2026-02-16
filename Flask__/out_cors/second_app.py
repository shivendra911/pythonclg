from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/data")
def data():
    return jsonify({
        "source": "second_app",
        "message": "Hello from port 9991"
    })

if __name__ == "__main__":
    app.run(port=9991, debug=True)
