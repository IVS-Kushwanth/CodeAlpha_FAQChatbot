import nltk
import string

from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

# Download required NLTK resources
nltk.download('punkt')
nltk.download('stopwords')

# Load stopwords once
stop_words = set(stopwords.words('english'))

def preprocess_text(text):

    # Handle empty input
    if text is None:
        return ""

    # Convert to lowercase
    text = str(text).lower().strip()

    # Tokenize
    tokens = word_tokenize(text)

    # Remove stopwords, punctuation, non-alphabetic words
    filtered_tokens = []

    for word in tokens:

        if (
            word not in stop_words
            and word not in string.punctuation
            and word.isalpha()
        ):
            filtered_tokens.append(word)

    # Prevent empty processed text
    if len(filtered_tokens) == 0:
        return text

    return " ".join(filtered_tokens)