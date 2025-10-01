
---

```markdown
# 🤖 Mini AI Chatbot

A **web-based AI chatbot** built with **Flask (backend)**, **React (frontend)**, and **Groq API** for LLM responses.  
It answers professional questions using either a local knowledge base or AI fallback, with **chat history** and **markdown-rendered responses**.

---

## 🚀 Features

- **Frontend**: React + TailwindCSS for a clean and responsive UI  
- **Backend**: Flask REST API with CORS support  
- **AI Integration**: Groq API for fallback responses  
- **Knowledge Base**: Local JSON dictionary with predefined Q&A pairs  
- **Markdown Support**: Rich text rendering of answers  
- **Chat History**: Stores the last 10 interactions  
- **Visual Cues**: Differentiates AI vs knowledge base answers  
- **Loading Animation**: Shows typing indicator while AI responds  

---

## 📂 Project Structure

```

mini-ai-chatbot/
│
├── backend/                    # Flask backend
│   ├── app.py                  # Main Flask app
│   ├── requirements.txt        # Python dependencies
│   └── .env                    # API keys (ignored by git)
│
├── frontend/                   # React frontend
│   ├── src/
│   │   ├── App.jsx             # Main React component
│   │   ├── App.css             # Styles
│   │   ├── index.jsx           # React entry point
│   │   └── components/         # Optional UI components
│   ├── package.json            # NPM dependencies
│   └── index.html              # HTML template
│
├── .gitignore                  # Ignore node_modules, env files, etc.
└── README.md                   # Project documentation

````

---

## ⚙️ Setup Instructions

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/TanujManikyala/mini-ai-chatbot.git
cd mini-ai-chatbot
````

---

### 2️⃣ Backend Setup (Flask)

```bash
cd backend
python -m venv venv
# Activate virtual environment
# Windows:
venv\Scripts\activate
# Linux/Mac:
source venv/bin/activate

pip install -r requirements.txt
```

Create a `.env` file inside `backend/`:

```
GROQ_API_KEY=your_groq_api_key_here
```

Run the backend server:

```bash
python app.py
```

The backend runs at: **[http://127.0.0.1:5000/](http://127.0.0.1:5000/)**

---

### 3️⃣ Frontend Setup (React)

```bash
cd ../frontend
npm install
npm start
```

Frontend runs at: **[http://localhost:3000/](http://localhost:3000/)**

---

## 🖥️ Usage

1. Open **[http://localhost:3000/](http://localhost:3000/)** in your browser.
2. Enter a professional question (e.g., `"How to prioritize tasks?"`).
3. The chatbot responds either from the **knowledge base** or via the **Groq LLM**.
4. Scroll through the last 10 interactions in the chat history.

---

## 🔒 Security & Best Practices

* **Never commit your `.env` file**; it contains sensitive API keys.
* `.gitignore` is preconfigured to ignore secrets and `node_modules`.
* API keys should be stored locally and never pushed to GitHub.

---

## 📦 Dependencies

### Backend (Python)

* Flask
* Flask-CORS
* fuzzywuzzy
* python-Levenshtein (optional, speeds up fuzzy matching)
* requests
* python-dotenv
* Groq Python SDK

Install with:

```bash
pip install -r backend/requirements.txt
```

### Frontend (JavaScript)

* React
* TailwindCSS (or plain CSS)
* Axios (if making HTTP calls)
* react-markdown
* remark-gfm

Install with:

```bash
npm install
```

---

## 🛠️ Future Enhancements

* Add **user authentication**
* Store chat history in a **database**
* Deploy to **cloud platforms** (Heroku, Vercel, Railway)
* Support **multiple AI models**
* Add **multi-language support**

---

## 👨‍💻 Author

**Tanuj Manikyala**
AI/ML Engineer | Passionate about building intelligent applications

---

```

