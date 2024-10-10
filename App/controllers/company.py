from App.database import db
from App.models import Company
from App.models.job_listing import JobListing
from sqlalchemy.exc import IntegrityError

# def create_Company(employer_id, companyName):
#     employer = Employer.query.get(employer_id)
#     if employer is None:
#         return None
#     newcompany = Company(companyName,employer)
#     try:
#         db.session.add(newcompany)
#         db.session.commit()
#     except IntegrityError as e:
#         db.session.rollback()
#         return None
#     else:
#         return newcompany

def create_Company(companyName):
    newcompany = Company(companyName)
    try:
        db.session.add(newcompany)
        db.session.commit()
    except IntegrityError as e:
        db.session.rollback()
        return None
    else:
        return newcompany


def create_job(company_id, title, description):
    company = Company.query.get(company_id)
    if company is None:
        return None
    newjob = JobListing(company_id=company_id, title=title, description=description)
    try:
        db.session.add(newjob)
        db.session.commit()
    except IntegrityError as e:
        db.session.rollback()
        return None
    else:
        return newjob
    

# def create_job(employer_id, title, description, company_id=None):
#     employer = Employer.query.get(employer_id)
#     if employer is None:
#         return None
#     newjob = JobListing(employer_id, title, description, company_id)
#     try:
#         db.session.add(newjob)
#         db.session.commit()
#     except IntegrityError as e:
#         db.session.rollback()
#         return None
#     else:
#         return newjob

# def list_CompanyEmployees(companyName):
#     _company = Company.query.filter_by(name = companyName)
#     if _company is None:
#         return None
    
#     employees = _company.employers
#     if employees is None:
#         return []
#     else :
#         return employees
