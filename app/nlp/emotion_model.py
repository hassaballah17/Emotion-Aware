def classify_emotion(tokens: list[str]) -> str:
    if "anxious" in tokens or "overwhelmed" in tokens:
        return "anxiety"
    if "sad" in tokens or "tired" in tokens:
        return "sadness"
    if "angry" in tokens or "furious" in tokens:
        return "anger"
    return "neutral"
