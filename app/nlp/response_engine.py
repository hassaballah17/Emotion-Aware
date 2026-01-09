import random

RESPONSES = {
    "anxiety": {
        "reflection": [
            "I see how heavy this feels right now.",
            "It sounds like a lot is pressing on you at once."
        ],
        "naming": [
            "There are signs of anxiety mixed with self-blame.",
            "This sounds like anxiety trying to regain control."
        ],
        "acceptance": [
            "It makes sense you feel this way given everything you've been carrying.",
            "Anyone in your position would feel overwhelmed."
        ],
        "reframe": [
            "Would you be open to looking at this more clearly, not more positively?",
            "We can slow this down and look at what’s actually in your control."
        ]
    },

    "sadness": {
        "reflection": [
            "I can sense how sad and tired you are.",
            "This feels heavy and draining."
        ],
        "naming": [
            "There are signs of sadness and emotional exhaustion.",
            "This sounds like deep emotional fatigue."
        ],
        "acceptance": [
            "It makes sense to feel this way after everything you’ve been through.",
            "Your feelings are valid, especially right now."
        ],
        "reframe": [
            "Would you like to talk more about what led here?",
            "We can gently untangle this together."
        ]
    },

    "anger": {
        "reflection": [
            "I can hear how intense this feels.",
            "This sounds deeply frustrating."
        ],
        "naming": [
            "There are clear signs of anger from feeling treated unfairly.",
            "This anger seems to come from crossed boundaries."
        ],
        "acceptance": [
            "Anyone would feel angry in a situation like this.",
            "Your anger makes sense given what happened."
        ],
        "reframe": [
            "Would it help to look at what exactly crossed the line?",
            "We can unpack this without dismissing how you feel."
        ]
    }
}

def build_response(emotion: str) -> dict:
    emotion = emotion.lower()

    if emotion not in RESPONSES:
        emotion = "sadness"  # safe default

    data = RESPONSES[emotion]

    return {
        "emotion": emotion,
        "reflection": random.choice(data["reflection"]),
        "naming": random.choice(data["naming"]),
        "acceptance": random.choice(data["acceptance"]),
        "reframe": random.choice(data["reframe"]),
    }
