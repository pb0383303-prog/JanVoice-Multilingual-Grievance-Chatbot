# JanVoice – Multilingual Citizen Grievance Assistant

**Hackathon problem:** HI-02 – Multilingual Citizen Grievance Chatbot  
**Track:** Human Impact

## Problem
Citizens may find it difficult to submit complaints in a language they are comfortable with. This prototype demonstrates a simple workflow to classify a grievance, route it to a relevant department, create a ticket, and let a citizen check its status.

## Features
- Complaint submission form with English and Telugu interface text.
- Prototype complaint classification for Water, Electricity, Roads, Sanitation, and Other.
- English TF-IDF + Logistic Regression classifier trained on illustrative examples.
- Telugu keyword-based category matching for a small set of common terms.
- Unique ticket ID generation and local CSV storage.
- Ticket status tracking and a basic admin dashboard.
- CSV export and status updates.

## Technology stack
Python, Streamlit, scikit-learn, pandas, CSV.

## Setup
1. Install Python 3.10 or newer.
2. Download or clone this repository.
3. Open a terminal in the project folder.
4. Create and activate a virtual environment (recommended):

   ```bash
   python -m venv .venv
   # Windows:
   .venv\Scripts\activate
   # macOS/Linux:
   source .venv/bin/activate
   ```

5. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

6. Run the app:

   ```bash
   streamlit run app.py
   ```

7. Open the local URL printed in the terminal.

## How to use
- Select **Submit a complaint**, enter a complaint, and create a ticket.
- Copy the generated ticket ID.
- Select **Track a complaint** and enter the ID to view its status.
- Select **Admin dashboard** to view records, update status, or download a CSV export.

## Model and evaluation notes
The English classifier is trained on a small, hand-written illustrative dataset included in `classifier.py`. The Telugu path currently uses keyword matching, not a trained Telugu language model or automatic translation. No meaningful benchmark accuracy is claimed. For a competition-ready evaluation, collect or create a larger labelled dataset, use a held-out test set, and report precision, recall, F1-score, and a confusion matrix.

## Data and privacy
This is a local demonstration. Records are stored in `data/complaints.csv` on the machine running the app. Do not enter real sensitive personal information. The app is not connected to government systems and does not actually forward complaints to public departments.

## AI tools
Disclose any AI tools used during development and describe how they were used. Update this section accurately before submission.

## Team
Add your team name and all member names here.
