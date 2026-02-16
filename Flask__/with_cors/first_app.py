from flask import Flask, render_template_string

app = Flask(__name__)

HTML = """
<!DOCTYPE html>
<html>
<body>
    <h2>First App (Frontend)</h2>
    <button onclick="loadData()">Call Second App</button>

    <pre id="output"></pre>

    <script>
        function loadData() {
            fetch("http://127.0.0.1:9999/api/data")
                .then(res => res.json())
                .then(data => {
                    document.getElementById("output").innerText =
                        JSON.stringify(data, null, 2);
                })
                .catch(err => {
                    document.getElementById("output").innerText = err;
                });
        }
    </script>
</body>
</html>
"""

@app.route("/")
def home():
    return render_template_string(HTML)

if __name__ == "__main__":
    app.run(port=5000, debug=True)
