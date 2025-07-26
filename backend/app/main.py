from fastapi import FastAPI, UploadFile, File, Depends
from fastapi.responses import JSONResponse
import numpy as np
import cv2
from sqlalchemy.orm import Session
from .database import SessionLocal, engine
from . import models, utils

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/detect")
async def detect(file: UploadFile = File(...), db: Session = Depends(get_db)):
    contents = await file.read()
    np_arr = np.frombuffer(contents, np.uint8)
    frame = cv2.imdecode(np_arr, cv2.IMREAD_COLOR)
    detections = utils.detect_emotion(frame)
    events = []
    for det in detections:
        evt = models.DetectionEvent(
            emotion=det['emotion'], confidence=str(det['confidence'])
        )
        db.add(evt)
        events.append(det)
    db.commit()
    return JSONResponse({"detections": events})

@app.get("/events")
def get_events(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    evts = db.query(models.DetectionEvent).offset(skip).limit(limit).all()
    return evts
