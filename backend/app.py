from flask import Flask, request, jsonify, send_from_directory
import os

from flask_cors import CORS  # allow frontend → backend calls
from utils import call_openai
from prompts import article_prompt, comment_prompt

app = Flask(__name__)
CORS(app)  # enable CORS for all domains in dev

@app.route("/generate_article", methods=["POST"])
def generate_article():
    data = request.get_json(force=True)
    print("/generate_article called with:", data)
    persona = data.get("persona")
    topic = data.get("topic")
    if not (persona and topic):
        return jsonify({"error": "'persona' and 'topic' are required"}), 400
    prompt = article_prompt(persona, topic)
    print(" Prompt ready to send:\n", prompt[:500], "...\n")
    article = call_openai(prompt)
    return {"persona": persona, "topic": topic, "article": article.strip()}

@app.route("/comment_article", methods=["POST"])
def comment_article():
    data = request.get_json(force=True)
    persona = data.get("persona")
    article = data.get("article")
    if not (persona and article):
        return jsonify({"error": "'persona' and 'article' are required"}), 400
    prompt = comment_prompt(persona, article)
    comment = call_openai(prompt)
    return {"persona": persona, "comment": comment.strip()}

@app.route("/")
def serve_index():
    return send_from_directory("static", "index.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001, debug=True)