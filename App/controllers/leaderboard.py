from App.models import Student, HoursCompleted, Accolade
from App.database import db
from App.controllers.accolade import award_accolade

def get_leaderboard():

    for student in Student.query.all():
        award_accolade(student)
    db.session.commit()


    results = db.session.query(
        Student.id,
        Student.first_name,
        Student.last_name,
        db.func.coalesce(db.func.sum(HoursCompleted.hours), 0).label("total_hours")
    ).outerjoin(HoursCompleted, (Student.id == HoursCompleted.student_id) & (HoursCompleted.status == 'confirmed'))\
     .group_by(Student.id).order_by(db.desc("total_hours")).all()


    leaderboard = []
    for rank, (student_id, first_name, last_name, total_hours) in enumerate(results, 1):
        accolade = Accolade.query.filter_by(student_id=student_id).first()
        accolade_str = accolade.accolade_level if accolade else "None"
        leaderboard.append({
            "rank": rank,
            "name": f"{first_name} {last_name}",
            "accolade": accolade_str,
            "total_hours": total_hours
        })
    return leaderboard
