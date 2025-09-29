from App.database import db
from App.models.accolade import Accolade
from App.models.hours_completed import HoursCompleted
from datetime import datetime
from sqlalchemy import func

def award_accolade(student):
    total_hours = db.session.query(func.sum(HoursCompleted.hours)).filter_by(student_id=student.id, status="confirmed").scalar() or 0

    if total_hours >= 50:
        level = "Gold"
    elif total_hours >= 25:
        level = "Silver"
    elif total_hours > 10:
        level = "Bronze"
    else:
        level = None

    if level:
        existing = Accolade.query.filter_by(student_id=student.id).first()
        if existing:
            existing.accolade_level = level
            existing.date_rewarded = datetime.utcnow()
        else:
            db.session.add(Accolade(student.id, level))
