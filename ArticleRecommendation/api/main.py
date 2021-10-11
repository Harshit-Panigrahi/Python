from flask import Flask, request, jsonify
from storage import storage
from demographic import top_20
from content_based import recommend

app = Flask(__name__)

@app.route("/")
def home():
  return jsonify({"data": storage["all"]})

@app.route("/star-article")
def star():
  title = request.args.get("title")
  if title in storage["all"]:
    if title in storage["starred"]:
      storage["starred"].remove(title)
    else:
      storage["starred"].append(title)
    return "Success"
  else:
    return "Article not found"

@app.route("/get-starred-articles")
def getStarred():
  return jsonify({"starred-articles": storage["starred"]})

@app.route("/get-recommendation")
def getRecommendation():
  title = request.args.get("title")
  return jsonify({"recommendations": recommend(title)})

@app.route("/top-20")
def top20():
  return jsonify({"top-20": top_20})

if __name__ == "__main__":
  app.run(debug=True)