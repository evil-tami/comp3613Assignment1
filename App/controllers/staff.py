from App.database import db
from App.models.staff import Staff
from App.models.student import Student
from App.models.hours_completed import HoursCompleted
from App.models.accolade import Accolade

def create_staff(first_name, last_name, password):
    staff = Staff(first_name=first_name, last_name=last_name, password=password)
    db.session.add(staff)
    db.session.commit()
    return staff

def review_hours(staff_id, student_id, request_index, confirm=True):
    staff = Staff.query.get(staff_id)
    student = Student.query.get(student_id)
    if not staff or not student:
        return None

    pending = HoursCompleted.query.filter_by(student_id=student.id, status="pending").all()
    if request_index < 0 or request_index >= len(pending):
        return None

    record = pending[request_index]
    record.status = "confirmed" if confirm else "denied"
    record.staff_id = staff.id
    db.session.commit()
    return record

def delete_student(staff_id, student_id):
    staff = Staff.query.get(staff_id)
    student = Student.query.get(student_id)
    if not staff or not student:
        return None

    HoursCompleted.query.filter_by(student_id=student.id).delete()
    Accolade.query.filter_by(student_id=student.id).delete()
    db.session.delete(student)
    db.session.commit()
    return student

