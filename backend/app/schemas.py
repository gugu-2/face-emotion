from pydantic import BaseModel
from datetime import datetime

class DetectionEventCreate(BaseModel):
    emotion: str
    confidence: float

class DetectionEvent(DetectionEventCreate):
    id: int
    timestamp: datetime

    class Config:
        orm_mode = True
