from App.database import db
from App.models import Job_Applicant,AppliedForJobs,JobListing
from sqlalchemy.exc import IntegrityError

def create_job_applicant(firstName, lastName, email, username ,password):
    newuser = Job_Applicant(firstName,lastName,email,username,password)
    try:
        db.session.add(newuser)
        db.session.commit()
    except IntegrityError as e:
        db.session.rollback()
        return None
    else:
        return newuser
    
def get_job_listings():
    job_listings = JobListing.query.all()
    return job_listings
    

def apply_job(job_applicant_id, job_listing_id):
    jobapplicant = JobListing.query.get(job_applicant_id)
    if jobapplicant is None:
        return None
    
    job_listing = JobListing.query.get(job_listing_id)
    if job_listing is None:
        return None
    appliedJobs = jobapplicant.applied_for_jobs
    if appliedJobs != None:
        if job_listing in appliedJobs:
            return None
        else:
            appliedJobs = AppliedForJobs(job_listing.id,job_listing.id)
