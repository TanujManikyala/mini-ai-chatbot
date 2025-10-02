# start.py
import os
from waitress import serve
# import Flask app object (adjust if different)
from backend.app import app

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    host = "0.0.0.0"
    print(f"Waitress serving on http://{host}:{port} (PORT env var = {os.environ.get('PORT')})")
    serve(app, host=host, port=port, threads=4)
