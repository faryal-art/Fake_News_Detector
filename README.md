# Fake News Detection 

## Project Overview
Fake news is a growing concern in the digital age. This project detects whether a news article is **real or fake** using machine learning. Users can enter news text in a web interface, and the app predicts its authenticity.  

This repository contains **two versions of the app**:  
1. **TF-IDF + Gradient Boosting Classifier**  
2. **Transformer-based model (DistilBERT)**  

---

## Live Web App Demo 🌐
- **TF-IDF + Gradient Boosting App**: [https://fakenewsdetector-g4qtvplekth8tcfyhwqqcy.streamlit.app/](#)  
- **Transformer-based App (DistilBERT)**: [Demo Link](#)  

> Test any news article in real time using the live demos.

---

## Features ✨
- User-friendly **Streamlit** interface  
- Preprocessing of news text (lowercase, remove punctuation, numbers, URLs, etc.)  
- Compare two approaches:  
  - Traditional **TF-IDF + Gradient Boosting**  
  - Modern **Transformer-based model**  
- Manual testing with custom input  
- Real-time prediction of news authenticity  

---

## Project Workflow 🛠️

### 1. Data Collection
- Datasets used:  
  - Fake news: `Fake.csv`  
  - Real news: `True.csv`  
- Source: [Kaggle Fake News Dataset](https://www.kaggle.com/datasets/jainpooja/fake-news-detection)

### 2. Data Preprocessing
- Lowercasing text  
- Removing punctuations, numbers, URLs, HTML tags  
- Cleaning text for model training  

### 3. Model Training
**TF-IDF + Gradient Boosting:**  
- Converted text into TF-IDF features  
- Trained classifiers: Logistic Regression, Decision Tree, Random Forest, Gradient Boosting  
- Selected **Gradient Boosting** based on highest accuracy  

**Transformer-based Ap**
