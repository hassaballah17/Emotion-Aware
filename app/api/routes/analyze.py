from fastapi import APIRouter
from app.api.schemas.analyze import AnalyzeRequest, EmotionResponse
from app.nlp.text_processing import preprocess_text
from app.nlp.emotion_model import classify_emotion
from app.nlp.response_engine import build_response

router = APIRouter()

@router.post("/analyze", response_model=EmotionResponse)
def analyze_text(request: AnalyzeRequest):
    tokens = preprocess_text(request.text)
    emotion = classify_emotion(tokens)
    response = build_response(emotion)
    return response
