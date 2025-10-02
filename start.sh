#!/bin/bash
# start.sh

# Use Railway's PORT environment variable, default to 8000 if not set
PORT=${PORT:-8000}
echo "Starting Flask app on port $PORT..."

# Start Gunicorn with 4 workers, binding to the specified port
#!/bin/bash
exec gunicorn backend.app:app --bind 0.0.0.0:$PORT --workers 4 --threads 2 --timeout 120
