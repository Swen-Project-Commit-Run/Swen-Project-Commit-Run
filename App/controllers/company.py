from App.database import db
from App.models import Company
from App.models import JobListing,Employer
from sqlalchemy.exc import IntegrityError

def create_Company(employer_id, companyName):
    print(f"Fetching employer with ID: {employer_id}")
    employer = Employer.query.get(employer_id)
    print(f"Retrieved employer: {employer}")


    if employer is None:
        print("employer not found")
        return None
    
    newcompany = Company(companyName, employer)
    employer.AttachCompany(newcompany.id)  # Attach the company to the employer

    try:
        db.session.add(newcompany)
        db.session.commit()  # Commit the new company to the database
        print("Company was added!")
    except IntegrityError as e:
        db.session.rollback()
        print("Company was NOT added!")
        return None
    
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
