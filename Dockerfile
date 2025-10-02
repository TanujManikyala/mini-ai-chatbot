# Dockerfile (place at repo root)
# Stage: build frontend
FROM node:18 AS frontend
WORKDIR /app/frontend
COPY frontend/package*.json ./
RUN npm install
COPY frontend/ ./
RUN npm run build

# Final image with Python runtime
FROM python:3.10-slim
WORKDIR /app

# (optional) minimal build deps for some wheels
RUN apt-get update && apt-get install -y --no-install-recommends build-essential \
    && rm -rf /var/lib/apt/lists/*

# Copy backend source
COPY backend/ ./backend

# Copy frontend build into backend/static (Flask serves backend/static)
COPY --from=frontend /app/frontend/dist ./backend/static

# Copy start.py (must exist in repo root)
COPY start.py .

# Install Python deps
RUN pip install --no-cache-dir flask flask-cors fuzzywuzzy python-Levenshtein requests openai waitress

# Expose for documentation only
EXPOSE 8000

# Run the Python entrypoint that reads PORT env var
CMD ["python", "start.py"]
