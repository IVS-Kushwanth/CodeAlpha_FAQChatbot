import pandas as pd

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

from preprocess import preprocess_text

# Load dataset
data = pd.read_csv("data/faq.csv", keep_default_na=False)

# Remove empty rows
data = data.dropna()

# Preprocess questions
data["processed_questions"] = data["question"].apply(preprocess_text)

# TF-IDF Vectorizer
vectorizer = TfidfVectorizer(
    ngram_range=(1, 2),   # unigrams + bigrams
    stop_words='english'
)

# Convert FAQ questions into vectors
X = vectorizer.fit_transform(data["processed_questions"])

def get_response(user_input):

    # Preprocess user input
    processed_input = preprocess_text(user_input)

    # Convert user input into vector
    user_vector = vectorizer.transform([processed_input])

    # Compute cosine similarity
    similarity = cosine_similarity(user_vector, X)

    # Find best matching question
    best_match_index = similarity.argmax()

    # Best similarity score
    best_score = similarity[0][best_match_index]

    # DEBUGGING OUTPUT
    print("\nUSER INPUT:", user_input)
    print("PROCESSED INPUT:", processed_input)
    print("BEST SCORE:", best_score)
    print(
        "MATCHED QUESTION:",
        data.iloc[best_match_index]["question"]
    )

    # Threshold check
    if best_score < 0.1:
        return "I couldn't find a matching FAQ. Try rephrasing your question."

    # Return answer
    answer = data.iloc[best_match_index]["answer"]

    return str(answer)