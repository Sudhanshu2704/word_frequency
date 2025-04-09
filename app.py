import streamlit as st
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from collections import Counter
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('punkt_tab')

# Ensure nltk data is downloaded
nltk.download('punkt')
nltk.download('stopwords')

st.title("📊 Word Frequency Analyzer")

# Text input
text = st.text_area("Paste your text here", height=250)

if st.button("Analyze"):
    if not text.strip():
        st.warning("Please enter some text to analyze.")
    else:
        # Preprocessing
        tokens = word_tokenize(text.lower())
        stop_words = set(stopwords.words('english'))
        filtered = [word for word in tokens if word.isalpha() and word not in stop_words]

        # Count and display top 10
        freq = Counter(filtered)
        st.subheader("🔝 Top 10 Most Common Words")
        for word, count in freq.most_common(10):
            st.write(f"**{word}**: {count}")
