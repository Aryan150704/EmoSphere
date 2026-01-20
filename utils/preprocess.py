import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
import string

nltk.download("punkt")
nltk.download("stopwords")
nltk.download("wordnet")

lemm = WordNetLemmatizer()
stop_words = set(stopwords.words("english"))

def preprocess_text(text):
    text = text.lower()
    tokens = nltk.word_tokenize(text)
    tokens = [lemm.lemmatize(t) for t in tokens if t not in stop_words and t not in string.punctuation]
    return tokens
