import csv
from pathlib import Path
from datetime import datetime
import uuid
import pandas as pd

DATA_FILE = Path(__file__).parent / "data" / "complaints.csv"
FIELDS = ["ticket_id", "name", "contact", "complaint", "category", "department", "status", "created_at"]

def _ensure_file():
    DATA_FILE.parent.mkdir(parents=True, exist_ok=True)
    if not DATA_FILE.exists():
        with DATA_FILE.open("w", newline="", encoding="utf-8") as f:
            csv.DictWriter(f, fieldnames=FIELDS).writeheader()

def create_ticket(name, contact, complaint, category, department):
    _ensure_file()
    ticket_id = "JV-" + uuid.uuid4().hex[:8].upper()
    row = {
        "ticket_id": ticket_id, "name": name.strip(), "contact": contact.strip(),
        "complaint": complaint.strip(), "category": category, "department": department,
        "status": "Open", "created_at": datetime.now().strftime("%Y-%m-%d %H:%M")
    }
    with DATA_FILE.open("a", newline="", encoding="utf-8") as f:
        csv.DictWriter(f, fieldnames=FIELDS).writerow(row)
    return ticket_id

def get_all_tickets():
    _ensure_file()
    return pd.read_csv(DATA_FILE, keep_default_na=False)

def get_ticket(ticket_id):
    df = get_all_tickets()
    matches = df[df["ticket_id"] == ticket_id]
    return matches.iloc[0].to_dict() if not matches.empty else None

def update_status(ticket_id, status):
    df = get_all_tickets()
    df.loc[df["ticket_id"] == ticket_id, "status"] = status
    df.to_csv(DATA_FILE, index=False, encoding="utf-8")
