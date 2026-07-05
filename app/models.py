from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from app import refrence_no
from app import db

class Complaint(db.Model):
    __tablename__ = 'complaints'
    id = db.Column(db.Integer, primary_key=True)
    reference = db.Column(db.String(20), nullable = False, unique = True)
    complaint_text = db.Column(db.Text, nullable = False)
    complaint_date = db.Column(db.DateTime, default=datetime.utcnow)
    status = db.Column(db.String(20), default='pending')

class BookingIssue(db.Model):
    __tablename__='booking_issue'
    id = db.Column(db.Integer, primary_key=True)
    reference = db.Column(db.String(20), nullable = False, unique = True)
    complaint_text = db.Column(db.Text, nullable = False)
    complaint_date = db.Column(db.DateTime, default=datetime.utcnow)
    status = db.Column(db.String(20), default='pending')

class ContactMessage(db.Model):
    __tablename__ = 'contact_messages'
    id = db.Column(db.Integer, primary_key=True)
    reference = db.Column(db.String(20),nullable = False, unique = True)
    message_text = db.Column(db.Text, nullable=False)
    message_date = db.Column(db.DateTime, default=datetime.utcnow)
    status = db.Column(db.String(20), default='new')   

def add_complaint(complaint_text):
    try:
        ref = refrence_no.generate_reference_no("complaint")
        complaint = Complaint(reference=ref, complaint_text=complaint_text)
        db.session.add(complaint)
        db.session.commit()
        return ref
    except Exception:
        db.session.rollback()
        return None


def add_bookIssue(complaint_text):
    try:
        ref = refrence_no.generate_reference_no("booking")
        complaint = BookingIssue(reference=ref, complaint_text=complaint_text)
        db.session.add(complaint)
        db.session.commit()
        return ref
    except Exception:
        db.session.rollback()
        return None


def add_Message(complaint_text):
    try:
        ref = refrence_no.generate_reference_no("message")
        message = ContactMessage(reference=ref,  message_text=complaint_text)
        db.session.add(message)
        db.session.commit()
        return ref
    except Exception:
        db.session.rollback()
        return None        

def delete_data(ref):
    prefix_map = {"bk": BookingIssue, "cp": Complaint, "ms": ContactMessage}
    model = prefix_map.get(ref[0:2])

    if not model:
        return False
    row = model.query.filter_by(reference=ref).first()
    if not row:
        return False
    db.session.delete(row)
    db.session.commit()
    return True   