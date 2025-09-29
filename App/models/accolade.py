from App.database import db
from werkzeug.security import generate_password_hash, check_password_hash  # For password hashing
from datetime import datetime

class Accolade(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    student_id = db.Column(db.Integer, db.ForeignKey('student.id'), nullable=False)
    accolade_level = db.Column(db.String(20), nullable=False)
    date_rewarded = db.Column(db.DateTime, default=datetime.utcnow)

    def __init__(self, student_id, accolade_level):
        self.student_id = student_id
        self.accolade_level = accolade_level
        self.date_rewarded = datetime.utcnow()

    __table_args__ = (db.UniqueConstraint('student_id', 'accolade_level', name='unique_accolade'),)
    #ensuring a student can have one accolade per level