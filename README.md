# JanVoice – Multilingual Citizen Grievance Chatbot

## Problem Statement
**HI-02 – Multilingual Citizen Grievance Chatbot**

## Project Overview
JanVoice is an AI-powered chatbot that helps citizens submit complaints in English and Telugu. It classifies complaints, assigns them to the appropriate government department, generates a unique ticket ID, and allows citizens to track complaint status.

## Key Features
- English complaint classification
- Telugu complaint classification
- Automatic department assignment
- Unique complaint ticket generation
- Complaint status tracking
- Admin dashboard
- Update complaint status
- Download complaint records as CSV

## Technology Stack
- Python
- Streamlit
- Scikit-learn
- Pandas
- TF-IDF
- Logistic Regression

## Project Structure
- `app.py` – Main Streamlit application
- `classifier.py` – Complaint classification
- `database.py` – Complaint storage and management
- `requirements.txt` – Project dependencies
- `data/complaints.csv` – Complaint records

## Installation and Setup

1. Clone the repository:

   `git clone https://github.com/pb0383303-prog/JanVoice-Multilingual-Grievance-Chatbot.git`

2. Open the project folder:

   `cd JanVoice-Multilingual-Grievance-Chatbot`

3. Install dependencies:

   `pip install -r requirements.txt`

4. Run the application:

   `streamlit run app.py`

## Testing
The prototype was tested with:
- English water complaints
- Telugu water complaints
- Ticket generation
- Complaint tracking
- Admin dashboard
- Complaint status updates

## Limitations
- The prototype uses a small illustrative training dataset.
- Telugu classification uses keyword-based rules.
- Classification confidence and accuracy require validation using a larger labelled dataset.
- This is a demonstration prototype, not a live government complaint system.

## Team Details
- Team Name: [pb0383303]
- Team Members: [Boppa Pavithra]

## AI Tools Used
[ChatGPT (OpenAI): Used for project planning, Python code assistance, debugging, and documentation.

GitHub: Used for source code hosting and project version management.]
## Screenshots

### Home Page
![JanVoice Home](Screenshot%202026-11-03%20213343.png)

### English Complaint
![English Complaint](Screenshot%202026-11-03%20213428.png)

### Telugu Complaint
![Telugu Complaint](Screenshot%202026-11-03%20213517.png)

### Ticket Tracking
![Ticket Tracking](Screenshot%202026-11-03%20213629.png)

### Admin Dashboard
![Admin Dashboard](Screenshot%202026-11-03%20213643.png)
