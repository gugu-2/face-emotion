import os

class Settings:
    DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://postgres:password@db:5432/emotions")
    EMOTION_MODEL_PATH = os.getenv("EMOTION_MODEL_PATH", "./models/emotion_model.pth")

settings = Settings()
