import nltk
from nltk.tokenize import word_tokenize
nltk.download('stopwords')
nltk.download('punkt_tab')
nltk.download('wordnet')
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
import string

stop_words = set(stopwords.words("english"))
lemmatizer = WordNetLemmatizer()

def preprocess_text(text: str) -> list[str]:
    text = text.lower()
    tokens = word_tokenize(text)

    return [
        lemmatizer.lemmatize(token)
        for token in tokens
        if token not in stop_words and token not in string.punctuation
    ]
