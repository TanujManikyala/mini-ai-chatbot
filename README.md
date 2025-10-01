
---

```markdown
# 🤖 Mini AI Chatbot

A simple **AI-powered chatbot** built with **Flask (backend)**, **React (frontend)**, and **Groq API** for LLM responses.  
It can answer professional questions using either an AI model or a local knowledge base.

---

## 🚀 Features
- 🔹 **Frontend**: React (with Tailwind for UI)
- 🔹 **Backend**: Flask REST API
- 🔹 **LLM**: Groq API integration
- 🔹 **Markdown Support**: Answers render nicely with formatting
- 🔹 **History**: Chat history with smooth scrolling
- 🔹 **Visual Separation**: Distinguishes AI answers vs Knowledge Base answers
- 🔹 **Loading Animation**: Shows spinner while AI responds

---

## 📂 Project Structure
```

mini-ai-chatbot/
│
├── backend/               # Flask backend
│   ├── app.py             # Main Flask app
│   ├── requirements.txt   # Python dependencies
│   └── .env               # API keys (ignored by git)
│
├── frontend/              # React frontend
│   ├── src/
│   │   ├── App.jsx        # Main React app
│   │   ├── App.css        # Styles
│   │   ├── index.jsx      # Entry point
│   │   └── components/    # Optional UI components
│   ├── package.json       # NPM dependencies
│   └── index.html         # HTML template
│
├── .gitignore             # Ignore env, node_modules, etc.
├── README.md              # Project documentation

````

---

## ⚙️ Setup Instructions

### 1️⃣ Clone the Repo
```bash
git clone https://github.com/TanujManikyala/mini-ai-chatbot.git
cd mini-ai-chatbot
````

---

### 2️⃣ Backend Setup (Flask)

```bash
cd backend
python -m venv venv
source venv/bin/activate   # On Linux/Mac
venv\Scripts\activate      # On Windows

pip install -r requirements.txt
```

👉 Create a `.env` file in `backend/`:

```
GROQ_API_KEY=your_groq_api_key_here
```

Run backend:

```bash
python app.py
```

Backend runs on **[http://127.0.0.1:5000/](http://127.0.0.1:5000/)**

---

### 3️⃣ Frontend Setup (React)

```bash
cd ../frontend
npm install
npm start
```

Frontend runs on **[http://localhost:3000/](http://localhost:3000/)**

---

## 🖥️ Usage

1. Open [http://localhost:3000](http://localhost:3000) in browser.
2. Ask professional questions (e.g., *"How to prioritize tasks?"*).
3. Bot responds using **Groq LLM** or **Knowledge Base**.

---

## 🔒 Environment & Security

* Never commit your `.env` file.
* `.gitignore` is configured to **ignore secrets**.
* Store your API keys locally only.

---

## 📦 Dependencies

### Backend

* Flask
* Flask-CORS
* Groq Python SDK
* Python-Dotenv

Install with:

```bash
pip install -r backend/requirements.txt
```

### Frontend

* React
* TailwindCSS
* Axios
* React-Markdown
* Remark-GFM

Install with:

```bash
npm install
```

---

## 🛠️ Future Enhancements

* Add user authentication
* Store chat history in database
* Deploy on cloud (Heroku, Vercel, or Railway)
* Add multiple AI model support

---

## 👨‍💻 Author

**Tanuj Manikyala**
🚀 AI/ML Engineer | Passionate about AI-powered applications

---

```

---



