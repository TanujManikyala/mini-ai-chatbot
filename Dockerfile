# Stage 1: Build frontend
FROM node:18 AS frontend
WORKDIR /app/frontend
COPY frontend/package*.json ./
RUN npm install
COPY frontend/ ./
RUN npm run build

# Stage 2: Build backend
FROM python:3.10-slim
WORKDIR /app
COPY backend/ ./backend
COPY --from=frontend /app/frontend/dist ./frontend/dist

RUN pip install --no-cache-dir flask flask-cors fuzzywuzzy python-Levenshtein openai gunicorn

COPY start.sh .
RUN chmod +x start.sh

# Dockerfile

# Copy the startup script into the container
COPY start.sh /app/start.sh

# Set the entry point to the startup script
ENTRYPOINT ["/app/start.sh"]
