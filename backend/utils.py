import nltk
nltk.download('rslp')
import re
from nltk.corpus import stopwords
from nltk.stem.rslp import RSLPStemmer
from PyPDF2 import PdfReader

nltk.download("stopwords")
stop_words = set(stopwords.words("portuguese"))
stemmer = RSLPStemmer()

def preprocess_text(text):
    text = text.lower()
    text = re.sub(r"[^\w\s]", "", text)

    words = text.split()
    words = [stemmer.stem(w) for w in words if w not in stop_words]

    return " ".join(words)


def read_file(file):
    if file.filename.endswith(".txt"):
        return file.read().decode("utf-8")

    if file.filename.endswith(".pdf"):
        reader = PdfReader(file)
        return " ".join(page.extract_text() for page in reader.pages)

    return ""
