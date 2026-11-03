import streamlit as st
import pandas as pd
from classifier import classify_complaint
from database import create_ticket, get_ticket, get_all_tickets

st.set_page_config(page_title="JanVoice | Citizen Grievance Assistant", page_icon="🏛️", layout="wide")

st.title("🏛️ JanVoice – Multilingual Citizen Grievance Assistant")
st.caption("Hackathon prototype | HI-02 | English + Telugu keyword support")
st.info("This is a demonstration prototype. It does not submit complaints to a real government department.")

with st.sidebar:
    st.header("Language / భాష")
    language = st.selectbox("Choose interface language", ["English", "తెలుగు (Telugu)"])
    st.divider()
    page = st.radio("Navigate", ["Submit a complaint", "Track a complaint", "Admin dashboard"])

if page == "Submit a complaint":
    if language == "English":
        st.subheader("Submit your grievance")
        name_label, contact_label, complaint_label = "Name (optional)", "Contact (optional)", "Describe your complaint"
        placeholder = "Example: There has been no water supply in our street for three days."
        submit_label = "Classify and create ticket"
    else:
        st.subheader("మీ ఫిర్యాదును నమోదు చేయండి")
        name_label, contact_label, complaint_label = "పేరు (ఐచ్ఛికం)", "సంప్రదింపు (ఐచ్ఛికం)", "మీ ఫిర్యాదును వివరించండి"
        placeholder = "ఉదాహరణ: మా వీధిలో మూడు రోజులుగా నీటి సరఫరా లేదు."
        submit_label = "ఫిర్యాదును గుర్తించి టికెట్ సృష్టించండి"

    with st.form("complaint_form"):
        name = st.text_input(name_label)
        contact = st.text_input(contact_label)
        complaint = st.text_area(complaint_label, placeholder=placeholder, height=150)
        submitted = st.form_submit_button(submit_label, type="primary")

    if submitted:
        if len(complaint.strip()) < 5:
            st.error("Please enter a little more detail." if language == "English" else "దయచేసి మరిన్ని వివరాలు నమోదు చేయండి.")
        else:
            category, department, confidence_note = classify_complaint(complaint)
            ticket_id = create_ticket(name, contact, complaint, category, department)
            st.success("Your demo ticket has been created!" if language == "English" else "మీ డెమో టికెట్ సృష్టించబడింది!")
            st.metric("Ticket ID", ticket_id)
            st.write(f"**Category:** {category}")
            st.write(f"**Assigned department:** {department}")
            st.caption(confidence_note)

elif page == "Track a complaint":
    st.subheader("Track complaint status / ఫిర్యాదు స్థితిని తెలుసుకోండి")
    ticket_id = st.text_input("Enter your ticket ID")
    if st.button("Check status"):
        ticket = get_ticket(ticket_id.strip().upper())
        if ticket:
            st.success("Ticket found")
            st.write(f"**Ticket ID:** {ticket['ticket_id']}")
            st.write(f"**Category:** {ticket['category']}")
            st.write(f"**Department:** {ticket['department']}")
            st.write(f"**Status:** {ticket['status']}")
            st.write(f"**Submitted:** {ticket['created_at']}")
            st.write(f"**Complaint:** {ticket['complaint']}")
        else:
            st.error("No ticket found. Check the ID and try again.")

else:
    st.subheader("Admin dashboard")
    st.caption("Demo records stored locally in data/complaints.csv")
    df = get_all_tickets()
    if df.empty:
        st.info("No complaints have been submitted yet.")
    else:
        c1, c2, c3 = st.columns(3)
        c1.metric("Total complaints", len(df))
        c2.metric("Open", int((df["status"] == "Open").sum()))
        c3.metric("Resolved", int((df["status"] == "Resolved").sum()))
        st.dataframe(df, use_container_width=True, hide_index=True)
        st.download_button("Download complaint records (CSV)", df.to_csv(index=False).encode("utf-8"), "complaints_export.csv", "text/csv")
        st.markdown("#### Update ticket status")
        selected = st.selectbox("Ticket ID", df["ticket_id"].tolist())
        new_status = st.selectbox("New status", ["Open", "In Progress", "Resolved"])
        if st.button("Update status"):
            from database import update_status
            update_status(selected, new_status)
            st.success(f"{selected} updated to {new_status}. Please refresh the page.")
