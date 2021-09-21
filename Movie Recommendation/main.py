from flask import Flask, request, jsonify
import csv
rows = []

with open("./api/movies_data.csv", encoding="utf-8") as f:
  reader = csv.reader(f)
  for row in reader:
    rows.append(row)

liked = []
disliked = []
watched = []

app = Flask(__name__)

@app.route("/")
def home():
  return "Hello World"

@app.route("/add-liked-movies", methods=["POST"])
def addlikedmovies():
  movie = request.args.get("name")
  liked.append(movie)
  return jsonify({
    "msg": "Movie successfuly added to liked movies"
  })

@app.route("/get-liked-movies")
def getlikedmovies():
  return jsonify({"liked":liked})

if __name__ == "__main__":
  app.run(debug=True)