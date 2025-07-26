import cv2
import torch
import torchvision.transforms as transforms
from .config import settings

# Load model
model = torch.load(settings.EMOTION_MODEL_PATH, map_location=torch.device('cpu'))
model.eval()

transform = transforms.Compose([
    transforms.ToPILImage(),
    transforms.Resize((48, 48)),
    transforms.Grayscale(),
    transforms.ToTensor(),
    transforms.Normalize((0.5,), (0.5,))
])

EMOTIONS = ['Angry', 'Disgust', 'Fear', 'Happy', 'Sad', 'Surprise', 'Neutral']

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

def detect_emotion(frame):
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    results = []
    for (x, y, w, h) in faces:
        roi = gray[y:y+h, x:x+w]
        img_t = transform(roi).unsqueeze(0)
        with torch.no_grad():
            output = model(img_t)
            conf, idx = torch.max(torch.softmax(output, dim=1), 1)
            emotion = EMOTIONS[idx]
            results.append({'box': [int(x), int(y), int(w), int(h)], 'emotion': emotion, 'confidence': float(conf)})
    return results
