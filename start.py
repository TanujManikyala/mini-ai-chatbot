# start.py (place at repo root)
from waitress import serve
from backend.app import app
import os

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    host = "0.0.0.0"
    print(f"Waitress serving on http://{host}:{port}")
    serve(app, host=host, port=port, threads=4)
