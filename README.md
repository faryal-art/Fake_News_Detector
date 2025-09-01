# Fake News Detection 

## Project Overview
Fake news is a growing concern in the digital age. This project detects whether a news article is **real or fake** using machine learning. Users can enter news text in a web interface, and the app predicts its authenticity.  

This repository contains **two versions of the app**:  
1. **TF-IDF + Gradient Boosting Classifier**  
2. **Transformer-based model (DistilBERT)**  

---

## Live Web App Demo 🌐
- **Transformer-based App (DistilBERT)**: [Click Here](https://fake-news-detector-g4qtvplekth8tcfyhwqqcy.streamlit.app/)
- **TF-IDF + Gradient Boosting App**: [Click Here](https://fakenewsdetector-g4qtvplekth8tcfyhwqqcy.streamlit.app/)  

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

**Transformer-based App:**  
- Used **DistilBERT** from Hugging Face  
- Fine-tuned for binary classification  
- Better semantic understanding of news context  

### 4. Model Evaluation
- Gradient Boosting accuracy: **0.9958**  
- Compared with other models  
- Transformer model provides even better context understanding  

### 5. Web App Development
- Built with **Streamlit**  
- Features:  
  - Text input box for manual testing  
  - Real-time prediction  
  - Clear feedback (Red = Fake, Green = Real)  

### 6. Deployment
- Deployed on **Streamlit Community Cloud**  
- GitHub repository: [Fake News Detector](https://github.com/faryal-art/Fake_News_Detector)  
- Live app available for testing both models  

---

## Project Structure 📂

```text
Fake_News_Detector/
│
├─ app.py                 # TF-IDF + Gradient Boosting Streamlit app
├─ app2.py                # Transformer-based Streamlit app
├─ model.pkl              # Gradient Boosting trained model
├─ vectorizer.pkl         # TF-IDF vectorizer
├─ requirements.txt       # Required packages
├─ README.md              # Project documentation
└─ datasets/              # Optional: original CSV files
```

---

## Usage Instructions 🖥️

1. Clone the repository:

```bash
git clone https://github.com/faryal-art/Fake_News_Detector.git
```
2. Navigate to the project folder:
 ```bash
cd Fake_News_Detector
```
3.Install dependencies:
```
pip install -r requirements.txt
```
4.Run the app:
```
streamlit run app.py
# or
streamlit run app2.py
```
5. Enter a news article and click Predict.

## Technologies & Libraries ⚡

- Python
- Streamlit (Web app)
- scikit-learn (Machine Learning)
- Transformers (DistilBERT for NLP)
- Pandas & NumPy (Data handling)
- Pickle (Saving and loading models)

## Conclusion ✅

This project demonstrates traditional ML and modern Transformer models for detecting fake news. Users can interactively test news articles in the web app. Both approaches are deployed for demonstration.

  





