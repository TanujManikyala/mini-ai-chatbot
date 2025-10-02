# Stage 1: Build frontend
FROM node:18 AS frontend
WORKDIR /app/frontend
COPY frontend/package*.json ./
RUN npm install
COPY frontend/ ./
RUN npm run build

# Stage 2: Final image with backend + static frontend
FROM python:3.10-slim
WORKDIR /app

# Install system deps needed for some python packages (optional)
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Copy backend code
COPY backend/ ./backend

# Copy frontend build into backend/static so Flask app can serve it
COPY --from=frontend /app/frontend/dist ./backend/static

# Copy start.py
COPY start.py .

# Install Python dependencies
RUN pip install --no-cache-dir \
    flask flask-cors fuzzywuzzy python-Levenshtein requests openai waitress

# Expose (informational)
EXPOSE 8000

# Runtime command: start.py will read PORT from env and start waitress
CMD ["python", "start.py"]
