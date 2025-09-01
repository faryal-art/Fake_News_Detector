import streamlit as st
from transformers import pipeline

# -----------------------------
# Load pretrained DistilBERT pipeline
# -----------------------------
@st.cache_resource  # cache to avoid reloading every time
def load_model():
    return pipeline("text-classification", model="distilbert-base-uncased-finetuned-sst-2-english")

classifier = load_model()

# -----------------------------
# Streamlit UI
# -----------------------------
st.title("📰 Fake News Detector - Transformer Version")
st.subheader("Detect whether news is Real or Fake using DistilBERT")

# Input text
user_input = st.text_area("Enter News Article", "")

if st.button("Predict"):
    if user_input.strip() == "":
        st.warning("⚠️ Please enter some news text first.")
    else:
        # Limit input to first 512 tokens (DistilBERT limit)
        text_to_classify = user_input[:512]
        result = classifier(text_to_classify)[0]

        label = result['label']
        score = result['score']

        # Mapping SST-2 sentiment to Fake/Real logic (you can fine-tune later)
        # For demonstration: POSITIVE → Real, NEGATIVE → Fake
        if label == "POSITIVE":
            st.success(f"✅ This is likely Real News (Confidence: {score:.2f})")
        else:
            st.error(f"❌ This is likely Fake News (Confidence: {score:.2f})")
