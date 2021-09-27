from flask import Flask, request, jsonify
from data import data

app = Flask(__name__)

liked = []

@app.route("/")
def home():
  return jsonify({"data": data})

@app.route("/add-liked-article", methods=["POST"])
def like():
  article = request.args.get("title")
  liked.append(article)
  return "Article successfuly added to Liked Articles."

@app.route("/get-liked-articles")
def getLiked():
  return jsonify({"liked": liked})

if __name__ == "__main__":
  app.run(debug=True)