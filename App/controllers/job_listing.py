from App.database import db
from App.models import JobListing,Employer


def CreateJobListing(employee_id,title,description):
    employer = Employer.query.get(employee_id)
    if employer is None:
        raise ValueError(f"Employer with ID {employee_id} does not exist.")
    jobListing = JobListing(employer.id,title,description,employer.company_id)
    db.session.add(jobListing)
    return db.session.commit()

def view_applicants_for_jobListing(jobListing_id):
    jobListing = JobListing.query.get(jobListing_id)
    if jobListing_id is None:
        raise ValueError(f'JobListing with ID {jobListing_id} does not exist.')
    
    applicants = jobListing.list_applicants()
    return applicants


