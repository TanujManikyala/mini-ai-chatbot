#!/bin/bash

# Set default port if not provided by Railway
#!/bin/bash
echo "Starting Flask app via Gunicorn..."
exec gunicorn backend.app:app \
    --bind 0.0.0.0:${PORT:-8000} \
    --workers 4 \
    --threads 2 \
    --timeout 120
