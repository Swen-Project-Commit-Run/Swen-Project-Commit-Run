from App.models import Employer
from App.models import Company
from App.database import db
from sqlalchemy.exc import IntegrityError

def create_employer(firstName, lastName, email, username ,password):
    newuser = Employer(firstName,lastName,email,username,password)
    try:
        db.session.add(newuser)
        db.session.commit()
    except IntegrityError as e:
        db.session.rollback()
        return None
    else:
        return newuser



    

