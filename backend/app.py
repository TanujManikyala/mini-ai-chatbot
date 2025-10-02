from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
from fuzzywuzzy import process
import json, os
import openai

GROQ_API_KEY = "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"

# Flask points to the React build folder inside Docker
app = Flask(__name__, static_folder="../frontend/dist", static_url_path="/")
CORS(app)

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def serve(path):
    file_path = os.path.join(app.static_folder, path)
    if path != "" and os.path.exists(file_path):
        return send_from_directory(app.static_folder, path)
    return send_from_directory(app.static_folder, 'index.html')

# Knowledge base
knowledge_base = {
    "How can I improve team productivity?": "Use daily stand-ups, set clear OKRs, and encourage time-blocking.",
    "Tips for remote work?": "Maintain a fixed schedule, use video check-ins, and set clear boundaries.",
    "How to prioritize tasks?": "Use the Eisenhower Matrix.",
    "How to manage startup funding?": "Track runway, maintain investor relations, and plan funding rounds early."
}

HISTORY_FILE = "history.json"
if not os.path.exists(HISTORY_FILE):
    with open(HISTORY_FILE, "w") as f:
        json.dump([], f)

def save_to_history(question, answer, source):
    with open(HISTORY_FILE, "r") as f:
        history = json.load(f)
    history.append({"question": question, "answer": answer, "source": source})
    history = history[-10:]
    with open(HISTORY_FILE, "w") as f:
        json.dump(history, f, indent=2)

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
        answer = response.output_text
        if not answer:
            answer = "I’m sorry, I didn’t catch that. How can I help you?"
        return answer
    except Exception as e:
        print("Groq API error:", e)
        return "❌ Error contacting AI model"

@app.route('/ask', methods=['POST'])
def ask():
    data = request.get_json()
    question = data.get('question', '').strip()
    best_match, score = process.extractOne(question, knowledge_base.keys())
    if score >= 80:
        answer = knowledge_base[best_match]
        source = 'knowledge_base ✅'
    else:
        answer = groq_fallback(question)
        source = 'AI model 🤖' if "Error" not in answer else 'error'
    save_to_history(question, answer, source)
    return jsonify({"answer": answer, "source": source})

@app.route('/history', methods=['GET'])
def get_history():
    with open(HISTORY_FILE, "r") as f:
        history = json.load(f)
    return jsonify(history)

if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 8000))  # Railway sets PORT automatically
    print(f"Starting Flask app on port {port}...")
    app.run(host="0.0.0.0", port=port)
