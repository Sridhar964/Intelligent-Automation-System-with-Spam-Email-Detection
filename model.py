# Task 4: Spam Detection using Machine Learning 

import pandas as pd
import re
import string

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score, classification_report

# -------------------------------
# LOAD DATASET
# -------------------------------

# Link: https://raw.githubusercontent.com/justmarkham/pycon-2016-tutorial/master/data/sms.tsv

df = pd.read_csv("sms.tsv", sep='\t', names=['label', 'text'])

# -------------------------------
# PREVIEW DATA
# -------------------------------
print("First 5 rows:\n", df.head())
print("\nTotal rows:", len(df))

# -------------------------------
# CONVERT LABELS (ham=0, spam=1)
# -------------------------------
df['label'] = df['label'].map({'ham': 0, 'spam': 1})

# -------------------------------
# TEXT CLEANING
# -------------------------------
def clean_text(text):
    text = text.lower()
    text = re.sub(r'\d+', '', text)  # remove numbers
    text = text.translate(str.maketrans('', '', string.punctuation))
    return text

df['text'] = df['text'].apply(clean_text)

# -------------------------------
# FEATURES & LABELS
# -------------------------------
X = df['text']
y = df['label']

# -------------------------------
# TF-IDF VECTORIZATION (Better than CountVectorizer)
# -------------------------------
vectorizer = TfidfVectorizer(stop_words='english', ngram_range=(1,2))
X_vectorized = vectorizer.fit_transform(X)

# -------------------------------
# TRAIN-TEST SPLIT
# -------------------------------
X_train, X_test, y_train, y_test = train_test_split(
    X_vectorized, y, test_size=0.2, random_state=42
)

# -------------------------------
# MODEL TRAINING
# -------------------------------
model = MultinomialNB()
model.fit(X_train, y_train)

# -------------------------------
# PREDICTION
# -------------------------------
y_pred = model.predict(X_test)

# -------------------------------
# EVALUATION
# -------------------------------
accuracy = accuracy_score(y_test, y_pred)

print("\n Accuracy:", accuracy)

print("\n Classification Report:\n")
print(classification_report(y_test, y_pred, target_names=['ham', 'spam']))

# -------------------------------
# CUSTOM TEST
# -------------------------------
sample = ["Congratulations! You won a free ticket worth 5000"]
sample_clean = [clean_text(sample[0])]
sample_vector = vectorizer.transform(sample_clean)

prediction = model.predict(sample_vector)

print("\n Custom Message:", sample[0])
print("🔍 Prediction:", "Spam" if prediction[0] == 1 else "Ham")