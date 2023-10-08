from flask import Flask, render_template, jsonify, request
from database import database

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/api/dht/multiple", methods=["GET"])
def multiple():
    limit = request.args.get("limit")
    limit = 20 if limit is None else int(limit)

    return jsonify(database.select_many_dht(limit))

@app.route("/api/dht/single", methods=["GET"])
def single():
    return jsonify(database.select_one_dht())

if __name__ == "__main__":
    app.run(debug=True)
