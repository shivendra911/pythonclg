
from flask import Flask, request, render_template_string
import re

app = Flask(__name__)

# 🔧 simple custom sanitizer
def simple_sanitize(text):
    if not text:
        return ""

    # remove script tags completely
    text = re.sub(r"<\s*script.*?>.*?<\s*/\s*script\s*>", "", text, flags=re.I | re.S)

    # remove event handlers like onclick, onerror etc
    text = re.sub(r'on\w+\s*=\s*"[^"]*"', "", text, flags=re.I)

    return text


@app.route("/escape")
def escape():
    data = request.args.get("data", "")
    return render_template_string("""
        <h2>Escaped Output (default)</h2>
        <p>{{ data }}</p>
    """, data=data)


@app.route("/no-escape")
def no_escape():
    data = request.args.get("data", "")
    return render_template_string("""
        <h2>No Escape (DANGEROUS)</h2>
        <p>{{ data | safe }}</p>
    """, data=data)


@app.route("/sanitized")
def sanitized():
    data = request.args.get("data", "")
    clean_data = simple_sanitize(data)
    return render_template_string("""
        <h2>Sanitized Output (custom)</h2>
        <p>{{ clean_data | safe }}</p>
    """, clean_data=clean_data)

@app.route("/")
def home():
    return """
        <h1>Home Page</h1>
        <ul>
            <li><a href="/escape">Escape Output</a></li>
            <li><a href="/no-escape">No Escape (Dangerous)</a></li>
            <li><a href="/sanitized">Sanitized Output</a></li>
        </ul>
    """


if __name__ == "__main__":
    app.run(debug=True)
