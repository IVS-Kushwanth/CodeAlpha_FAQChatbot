# CodeAlpha FAQ Chatbot (Streamlit)

A lightweight FAQ chatbot using an NLP preprocessing step and TF-IDF cosine-similarity matching.

## Project structure
- `app.py` – Streamlit UI
- `chatbot.py` – FAQ matching logic
- `preprocess.py` – text normalization + CSV loader
- `data/faq.csv` – your knowledge base

## Setup
```bash
pip install -r requirements.txt
```

## Run
```bash
streamlit run app.py
```

Then open the shown local URL in your browser.

## Add your own FAQs
Edit `data/faq.csv` and keep these columns:
- `question`
- `answer`

Each new row becomes a searchable FAQ.

## Notes
- The app uses TF-IDF (with uni/bi-grams) + cosine similarity.
- If the answer doesn’t appear, raise/lower the similarity threshold in the sidebar or rephrase the question.

