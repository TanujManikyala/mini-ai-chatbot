from flask import Flask, request, jsonify
from flask_cors import CORS
from fuzzywuzzy import process
import json, os
import requests

app = Flask(__name__)
CORS(app)
from flask import send_from_directory

@app.route('/')
def serve():
    return send_from_directory('static', 'index.html')

# --- Knowledge Base ---
knowledge_base = {
    "How can I improve team productivity?": "Use daily stand-ups, set clear OKRs, and encourage time-blocking.",
    "Tips for remote work?": "Maintain a fixed schedule, use video check-ins, and set clear boundaries.",
    "How to prioritize tasks?": "Use the Eisenhower Matrix: urgent-important, not urgent-important, etc.",
    "How to manage startup funding?": "Track runway, maintain investor relations, and plan funding rounds early.",
    "How to ask someone's name respectfully?": "Politely say 'May I know your name?' or 'Could you tell me your name, please?'",
    "How to handle remote meetings effectively?": "Set an agenda, mute when not speaking, and follow up with notes.",
    "Tips for managing stress at work?": "Take short breaks, prioritize tasks, and practice mindfulness.",
    "How to delegate tasks?": "Assign based on skill, provide clear instructions, and set deadlines."
}

# --- History file ---
HISTORY_FILE = "history.json"
if not os.path.exists(HISTORY_FILE):
    with open(HISTORY_FILE, "w") as f:
        json.dump([], f)

def save_to_history(question, answer, source):
    with open(HISTORY_FILE, "r") as f:
        history = json.load(f)
    history.append({"question": question, "answer": answer, "source": source})
    history = history[-10:]  # keep only last 10
    with open(HISTORY_FILE, "w") as f:
        json.dump(history, f, indent=2)

# --- Groq LLM Fallback ---

def groq_fallback(question):
    try:
        import openai
        client = openai.OpenAI(
            api_key=os.getenv("GROQ_API_KEY"),
            base_url="https://api.groq.com/openai/v1"
        )
        response = client.responses.create(
            model="openai/gpt-oss-20b",
            input=question
        )
        # response.output_text should have the final answer
        answer = response.output_text
        if not answer:  # fallback if empty
            answer = "I’m sorry, I didn’t catch that. How can I help you?"
        return answer
    except Exception as e:
        print("Groq API error:", e)
        return "❌ Error contacting AI model"


# --- Flask routes ---
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
    port = int(os.environ.get("PORT", 5000))  # use Railway PORT if provided
    app.run(host="0.0.0.0", port=port)
