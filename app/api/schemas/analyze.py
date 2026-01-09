from pydantic import BaseModel

class AnalyzeRequest(BaseModel):
    text: str

class EmotionResponse(BaseModel):
    emotion: str
    reflection: str
    naming: str
    acceptance: str
    reframe: str
