# ---------- Build Frontend ----------
FROM node:18 AS frontend
WORKDIR /app/frontend
COPY frontend/ .
RUN npm install
RUN npm run build   # builds React app into /dist

# ---------- Backend with Flask ----------
FROM python:3.10 AS backend
WORKDIR /app

# Install Python dependencies
COPY backend/requirements.txt .
RUN pip install -r requirements.txt

# Copy backend code
COPY backend/ ./backend

# Copy frontend build into backend static folder
COPY --from=frontend /app/frontend/dist ./backend/static

# Flask runs from backend
ENV FLASK_APP=backend/app.py
ENV FLASK_RUN_HOST=0.0.0.0
ENV FLASK_ENV=production

EXPOSE 5000
CMD ["flask", "run"]
