# Face Emotion Detection for Security

## Overview
This application captures live video feed, performs real-time emotion detection on faces, logs events to a database, and provides a dashboard to monitor threats and behavioral signals.

## Tech Stack
- **Backend**: Python, FastAPI, OpenCV, PyTorch (for emotion model), SQLAlchemy, PostgreSQL
- **Frontend**: React, WebRTC, Axios
- **Database**: PostgreSQL
- **Containerization**: Docker & Docker Compose

## Setup
1. Clone repository
2. Download or train an emotion detection model and place it at `backend/app/models/emotion_model.pth` (see backend/app/utils.py for path)
3. `docker-compose up --build`
4. Visit `http://localhost:3000`

## Endpoints
- `POST /detect` — accepts video frames, returns detected face emotions
- `GET /events` — retrieves logged events

## Testing
```bash
cd backend
pytest -v
```