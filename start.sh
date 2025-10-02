#!/bin/sh
PORT=${PORT:-8000}
echo "Starting gunicorn on 0.0.0.0:$PORT"
exec gunicorn backend.app:app --bind 0.0.0.0:"$PORT" --workers 4 --threads 2 --timeout 120
