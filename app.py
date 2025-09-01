import streamlit as st
import pandas as pd
import pickle
import re,string

#load model and vectorizer
model = pickle.load(open('model.pkl','rb'))
vectorizer=pickle.load(open('vectorizer.pkl','rb'))

# function for new's text preprocessing
def preprocess_text(text):
  text= text.lower()
  text=re.sub('\[.*?]','',text)
  text=re.sub('\\W',' ',text)
  text=re.sub('https?://\\S+|www\\.\S+','',text)
  text=re.sub('<.*?>+','',text)
  text=re.sub('[%s]' % re.escape(string.punctuation), '', text)
  text=re.sub('\n', '', text)
  text=re.sub('\w*\d\w*', '', text)
  return text


# streamlit web app UI
st.title("Fake News Detector")
st.subheader("Detect whether a news article is Real or Fake using Gradient Boosting")

# text box for input
user_input = st.text_area('Enter News Article','')

if st.button('Predict'):
    if user_input.strip()=='':
        st.warning("Please enter some news text first")
    else:
        c_text=preprocess_text(user_input)
        words=c_text.split()
        words_in_vocab = [w for w in words if w in vectorizer.vocabulary_]
        st.write("📝 Words in vectorizer vocabulary:", words_in_vocab)
        st.write("ℹ️ Number of recognized words:", len(words_in_vocab))
        if len(words_in_vocab) < 5:
            st.warning("⚠️ Very few words recognized. Prediction may be unreliable.")
        v_text=vectorizer.transform([c_text])
        prediction=model.predict(v_text)[0]


        if prediction == 0:
            st.error(" Fake News Detected")
        else:
            st.success(" This is Real News")