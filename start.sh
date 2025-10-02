#!/bin/bash
# Start the Flask backend with Gunicorn
gunicorn backend.app:app --bind 0.0.0.0:$PORT
