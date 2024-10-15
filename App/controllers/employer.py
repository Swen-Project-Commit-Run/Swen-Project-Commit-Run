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



    
def get_job_listings(employer_id):
    employer = Employer.query.get(employer_id)
    if employer is None:
        raise ValueError(f"Employer with ID {employer_id} does not exist.")

    if employer.jobListings is None:
        return employer.jobListings
    else:
        return []
