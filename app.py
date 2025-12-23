from flask import Flask, request, jsonify
from flask_cors import CORS

app=Flask(__name__)
CORS(app)


@app.route("/voice-llm", methods=["POST"])
def voice_llm():
    data = request.json
    prompt = data.get("prompt")
    llm_name = data.get("llm", "ChatGPT")

    llm = globals()[llm_name]()
    result = llm.invoke(prompt)

    return jsonify({ "response": result })
