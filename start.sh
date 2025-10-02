#!/bin/sh

# Use the PORT environment variable provided by Railway, default to 8000
PORT=${PORT:-8000}

# Start the Flask app with Gunicorn
gunicorn backend.app:app --bind 0.0.0.0:$PORT
