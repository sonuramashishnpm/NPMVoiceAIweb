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


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=False)
