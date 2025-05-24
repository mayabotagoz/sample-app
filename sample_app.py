from flask import Flask, render_template, jsonify

app = Flask(__name__)

@app.route("/")
def main():
    return render_template("index.html")

@app.route("/status")
def status():
    return jsonify({
        "status": "running",
        "version": "1.0",
        "uptime": "OK"
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5050)

