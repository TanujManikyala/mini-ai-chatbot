#!/bin/bash
# Use Railway's PORT if available, otherwise default 8000
#!/bin/bash
PORT=${PORT:-8000}  # Default to 8000 if PORT is not set
echo "Starting Flask app on port $PORT..."
exec gunicorn backend.app:app --bind 0.0.0.0:$PORT --workers 4 --threads 2 --timeout 120
