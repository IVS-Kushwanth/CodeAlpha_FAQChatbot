import string

# Simple stopword list
stop_words = {
    "is", "am", "are", "the", "a", "an",
    "what", "how", "do", "does", "can",
    "i", "you", "to", "of", "and", "in"
}

def preprocess_text(text):

    # Handle empty input
    if text is None:
        return ""

    # Lowercase
    text = str(text).lower().strip()

    # Remove punctuation
    text = text.translate(
        str.maketrans('', '', string.punctuation)
    )

    # Split into words
    words = text.split()

    # Remove stopwords
    filtered_words = [
        word for word in words
        if word not in stop_words
    ]

    # Prevent empty string
    if len(filtered_words) == 0:
        return text

    return " ".join(filtered_words)