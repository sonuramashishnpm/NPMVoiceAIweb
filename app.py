from flask import Flask, render_template, request, jsonify
from npmai import Ollama  # Your npmai LLM

app = Flask(__name__, template_folder="templates", static_folder="static")

# Initialize LLM once
llm = Ollama()
MODEL_NAME = "llama3.2"  # fixed model

# Route to serve HTML page
@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")


# Route to handle voice input from frontend
@app.route("/voice-llm", methods=["POST"])
def voice_llm():
    data = request.get_json()
    prompt = data.get("prompt", "")

    try:
        # Use npmai to invoke LLM with fixed model
        result = llm.invoke(prompt, MODEL_NAME)
        response = str(result)  # make sure it's string for JSON
    except Exception as e:
        response = f"Error: {str(e)}"

    return jsonify({"response": response})


if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=False)