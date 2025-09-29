from App.database import db
from werkzeug.security import generate_password_hash, check_password_hash  # For password hashing
from datetime import datetime

class HoursCompleted(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    student_id = db.Column(db.Integer, db.ForeignKey('student.id'), nullable=False)
    staff_id = db.Column(db.Integer, db.ForeignKey('staff.id'), nullable=True)  # staff optional
    hours = db.Column(db.Integer, nullable=False)
    activity = db.Column(db.String(120), nullable=False)
    status = db.Column(db.String(20), nullable=False, default="pending")
    date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    def __init__(self, student_id, hours, activity, status="pending", staff_id=None):
        self.student_id = student_id
        self.hours = hours
        self.activity = activity
        self.status = status
        self.staff_id = staff_id

