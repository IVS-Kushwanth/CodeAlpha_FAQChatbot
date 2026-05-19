import streamlit as st
from chatbot import get_response

# Page configuration
st.set_page_config(
    page_title="FAQ Chatbot",
    page_icon="🤖",
    layout="centered"
)

st.title("🤖 FAQ Chatbot")
with st.sidebar:

    st.header("About")

    st.write("""
    This FAQ chatbot uses:
    - NLP preprocessing
    - TF-IDF vectorization
    - Cosine similarity

    Built using:
    - Python
    - Streamlit
    - Scikit-learn
    """)

    if st.button("Clear Chat"):
        st.session_state.messages = []
        st.rerun()
st.write("Ask questions related to the FAQ dataset.")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# User input
user_input = st.chat_input("Type your question here...")

# Process user input
if user_input:

    # Store user message
    st.session_state.messages.append(
        {"role": "user", "content": user_input}
    )

    # Get bot response
    response = get_response(user_input)

    # Store bot response
    st.session_state.messages.append(
        {"role": "assistant", "content": response}
    )

# Display chat history
for message in st.session_state.messages:

    with st.chat_message(message["role"]):
        st.write(message["content"])