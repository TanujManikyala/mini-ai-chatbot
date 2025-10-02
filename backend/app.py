# backend/app.py
from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
from fuzzywuzzy import process
import json, os
import openai

# Hard-coded fallback key (ONLY for local testing). Prefer using env var in production.
HARDCODED_GROQ_KEY = "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"

# Read from env first (recommended). If not present, fall back to hard-coded value.
GROQ_API_KEY = os.environ.get("GROQ_API_KEY", HARDCODED_GROQ_KEY)

# Flask app expects the frontend build to be in backend/static
app = Flask(__name__, static_folder="static", static_url_path="/")
CORS(app)

# Serve frontend single-page app (SPA)
@app.route("/", defaults={"path": ""})
@app.route("/<path:path>")
def serve(path):
    if path and os.path.exists(os.path.join(app.static_folder, path)):
        return send_from_directory(app.static_folder, path)
    return send_from_directory(app.static_folder, "index.html")


# --- Knowledge base ---
knowledge_base = {
    "How can I improve team productivity?": "Use daily stand-ups, set clear OKRs, and encourage time-blocking.",
    "Tips for remote work?": "Maintain a fixed schedule, use video check-ins, and set clear boundaries.",
    "How to prioritize tasks?": "Use the Eisenhower Matrix.",
    "How to manage startup funding?": "Track runway, maintain investor relations, and plan funding rounds early."
}

# History file (keeps last 10)
HISTORY_FILE = "history.json"
if not os.path.exists(HISTORY_FILE):
    with open(HISTORY_FILE, "w") as f:
        json.dump([], f)

def save_to_history(question, answer, source):
    try:
        with open(HISTORY_FILE, "r") as f:
            history = json.load(f)
    except Exception:
        history = []
    history.append({"question": question, "answer": answer, "source": source})
    history = history[-10:]
    with open(HISTORY_FILE, "w") as f:
        json.dump(history, f, indent=2)


# --- GROQ fallback using the OpenAI-compatible client (groq) ---
def groq_fallback(question):
    try:
        client = openai.OpenAI(
            api_key=GROQ_API_KEY,
            base_url="https://api.groq.com/openai/v1"
        )
        response = client.responses.create(
            model="openai/gpt-oss-20b",
            input=question
        )
        # client.responses.create typically provides an attribute with text; we use response.output_text
        answer = getattr(response, "output_text", None)
        if not answer:
            # Try to pull from alternative fields (defensive)
            if hasattr(response, "output"):
                # some clients return structured output
                try:
                    answer = response.output[0].content[0].text
                except Exception:
                    answer = None
        return answer or "I’m sorry, I didn’t catch that. How can I help you?"
    except Exception as e:
        # Log server-side — keep response concise for client
        print("Groq API error:", e)
        return "❌ Error contacting AI model"


# --- API routes ---
@app.route("/ask", methods=["POST"])
def ask():
    data = request.get_json() or {}
    question = (data.get("question") or "").strip()
    if not question:
        return jsonify({"answer": "Please send a question.", "source": "error"}), 400

    best_match, score = process.extractOne(question, knowledge_base.keys())
    if score and score >= 80:
        answer = knowledge_base[best_match]
        source = "knowledge_base ✅"
    else:
        answer = groq_fallback(question)
        source = "AI model 🤖" if "Error" not in answer else "error"

    save_to_history(question, answer, source)
    return jsonify({"answer": answer, "source": source})


@app.route("/history", methods=["GET"])
def get_history():
    try:
        with open(HISTORY_FILE, "r") as f:
            history = json.load(f)
    except Exception:
        history = []
    return jsonify(history)


# --- Run locally (debug) ---
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    print(f"Starting Flask dev server on 0.0.0.0:{port}")
    app.run(host="0.0.0.0", port=port)
