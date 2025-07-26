from sqlalchemy import Column, Integer, String, DateTime, Float
from .database import Base
import datetime

class DetectionEvent(Base):
    __tablename__ = "events"
    id = Column(Integer, primary_key=True, index=True)
    timestamp = Column(DateTime, default=datetime.datetime.utcnow)
    emotion = Column(String, index=True)
    confidence = Column(Float)
