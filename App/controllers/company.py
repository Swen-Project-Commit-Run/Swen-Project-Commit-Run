from App.database import db
from App.models import Company
from App.models import JobListing,Employer
from sqlalchemy.exc import IntegrityError

def create_Company(employer_id, companyName):
    employer = Employer.query.get(employer_id)
    if employer is None:
        return None
    newcompany = Company(companyName,employer)
    try:
        db.session.add(newcompany)
        db.session.commit()
    except IntegrityError as e:
        db.session.rollback()
        return None
    else:
        return newcompany




def list_CompanyJobLisings(companyName):
    _company = Company.query.filter_by(name = companyName)
    if _company is None:
        return None
    
    jobListing = _company.jobListings
    if jobListing is None:
        return []
    else :
        return jobListing
