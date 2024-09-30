from App.models import Applicant
from App.database import db

def create_applicant(username, email, password):
    newuser = Applicant(username=username, email=email, password=password)
    db.session.add(newuser)
    db.session.commit()
    return newuser