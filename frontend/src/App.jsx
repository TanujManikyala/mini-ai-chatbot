import React, { useState, useRef, useEffect } from 'react';
import ReactMarkdown from 'react-markdown';
import remarkGfm from 'remark-gfm';
import './App.css';

export default function App() {
  const [question, setQuestion] = useState('');
  const [history, setHistory] = useState([]);
  const [loading, setLoading] = useState(false);
  const chatEndRef = useRef(null);

  const ask = async () => {
    if (!question.trim()) return;
    setLoading(true);

    const userQuestion = question;
    setHistory([{ q: userQuestion, a: '', source: 'user' }, ...history].slice(0, 10));
    setQuestion('');

    try {
      const res = await fetch('http://127.0.0.1:5000/ask', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ question: userQuestion }),
      });
      const data = await res.json();
      const answer = data.answer;
      const source = data.source; // can be 'knowledge_base ✅' or 'AI model 🤖'

      setHistory((prev) =>
        prev.map((h) =>
          h.q === userQuestion && h.source === 'user'
            ? { ...h, a: answer, source }
            : h
        )
      );
    } catch (e) {
      setHistory((prev) =>
        prev.map((h) =>
          h.q === userQuestion && h.source === 'user'
            ? { ...h, a: '❌ Error contacting server', source: 'error' }
            : h
        )
      );
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    chatEndRef.current?.scrollIntoView({ behavior: 'smooth' });
  }, [history]);

  return (
    <div className="container">
      <h2>💬 Mini AI Chatbot — Professional Q&A</h2>

      <div className="input-container">
        <input
          value={question}
          onChange={(e) => setQuestion(e.target.value)}
          onKeyDown={(e) => e.key === 'Enter' && ask()}
          placeholder="Ask a professional question (e.g., 'How to prioritize tasks?')"
        />
        <button onClick={ask} disabled={loading || !question.trim()}>
          {loading ? <span className="typing">💭 Thinking...</span> : 'Ask'}
        </button>
      </div>

      <div className="chat-history">
        {history.length === 0 && <div className="no-msg">✨ No questions yet — try one!</div>}

        {history.map((item, idx) => (
          <div
            key={idx}
            className={`chat-bubble ${
              item.source === 'bot'
                ? 'bot'
                : item.source === 'error'
                ? 'error'
                : item.source === 'AI model 🤖'
                ? 'ai-bot'
                : 'user'
            }`}
          >
            <div className="message">
              {item.source === 'user'
                ? '🧑 You: '
                : item.source === 'bot'
                ? '🤖 Bot: '
                : item.source === 'AI model 🤖'
                ? '🤖 AI: '
                : ''}
              {item.a ? (
                <ReactMarkdown remarkPlugins={[remarkGfm]}>{item.a}</ReactMarkdown>
              ) : (
                item.q
              )}
            </div>
            {(item.source === 'bot' || item.source === 'AI model 🤖') && (
              <div className="source">
                source: {item.source === 'bot' ? 'knowledge_base ✅' : 'AI model 🤖'}
              </div>
            )}
          </div>
        ))}

        {loading && (
          <div className="chat-bubble bot">
            <div className="message typing-dots">
              🤖 Bot is typing<span className="dot">.</span>
              <span className="dot">.</span>
              <span className="dot">.</span>
            </div>
          </div>
        )}

        <div ref={chatEndRef} />
      </div>
    </div>
  );
}
