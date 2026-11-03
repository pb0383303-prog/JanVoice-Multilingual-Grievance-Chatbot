"""Lightweight bilingual grievance classifier for the hackathon MVP.

English complaints use a TF-IDF + Logistic Regression model trained on
small, illustrative examples. Telugu support uses a transparent keyword
fallback. Replace/expand the sample data and evaluate on a real dataset
before making operational claims.
"""
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

TRAINING = [
    ("no water supply in my street", "Water"),
    ("water pipe is leaking", "Water"),
    ("dirty drinking water", "Water"),
    ("there is no water for three days", "Water"),
    ("power cut in our area", "Electricity"),
    ("electricity bill is incorrect", "Electricity"),
    ("street light is not working", "Electricity"),
    ("transformer is making noise", "Electricity"),
    ("road has many potholes", "Roads"),
    ("road is damaged and unsafe", "Roads"),
    ("need repair of the street road", "Roads"),
    ("garbage is not collected", "Sanitation"),
    ("drain is blocked and overflowing", "Sanitation"),
    ("sewage water is on the road", "Sanitation"),
    ("public area is full of waste", "Sanitation"),
    ("bus stop has no shelter", "Other"),
    ("please help with a certificate", "Other"),
    ("requesting information about local office", "Other"),
]
MODEL = Pipeline([
    ("tfidf", TfidfVectorizer(ngram_range=(1, 2), lowercase=True)),
    ("clf", LogisticRegression(max_iter=1000, class_weight="balanced")),
])
MODEL.fit([x for x, _ in TRAINING], [y for _, y in TRAINING])

DEPARTMENTS = {
    "Water": "Water Supply Department",
    "Electricity": "Electricity Board",
    "Roads": "Roads & Public Works Department",
    "Sanitation": "Sanitation / Municipal Department",
    "Other": "General Citizen Services",
}

TE_WORDS = {
    "Water": ["నీరు", "నీటి", "తాగునీరు", "నీళ్లు", "పైపు"],
    "Electricity": ["కరెంట్", "విద్యుత్", "విద్యుత్‌", "లైట్", "ట్రాన్స్‌ఫార్మర్"],
    "Roads": ["రోడ్డు", "రహదారి", "గుంతలు", "గుంత"],
    "Sanitation": ["చెత్త", "మురుగు", "డ్రైనేజ్", "కాలువ", "శుభ్రత"],
}

def classify_complaint(text: str):
    cleaned = text.strip()
    for category, words in TE_WORDS.items():
        if any(word in cleaned for word in words):
            return category, DEPARTMENTS[category], "Matched Telugu complaint keywords (prototype rule-based classification)."
    prediction = MODEL.predict([cleaned])[0]
    probabilities = MODEL.predict_proba([cleaned])[0]
    confidence = float(max(probabilities))
    note = f"Prototype NLP classifier confidence: {confidence:.0%}. Validate with a larger labelled dataset."
    return prediction, DEPARTMENTS[prediction], note
