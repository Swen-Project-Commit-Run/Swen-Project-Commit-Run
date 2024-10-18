from App.database import db
from App.models import Job_Applicant,AppliedForJobs,JobListing
from sqlalchemy.exc import IntegrityError

from App.models.user import User

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
    # Fetch the applicant based on the applicant ID
    applicant = User.query.get(job_applicant_id)  # Assuming applicants are in the User model
    if applicant is None:
        print(f"Applicant with ID {job_applicant_id} does not exist.")
        return None

    # Fetch the job listing based on the job listing ID
    job_listing = JobListing.query.get(job_listing_id)
    if job_listing is None:
        print(f"Job listing with ID {job_listing_id} does not exist.")
        return None

    # Check if the applicant has already applied for this job listing
    existing_application = AppliedForJobs.query.filter_by(
        job_id=job_listing_id, applicant_id=job_applicant_id
    ).first()

    if existing_application is not None:
        print(f"Applicant {job_applicant_id} has already applied for job listing {job_listing_id}.")
        return None
    
    # Create a new application record
    new_application = AppliedForJobs(job_id=job_listing.id, applicant_id=applicant.id)
    
    # Add and commit the new application to the database
    db.session.add(new_application)
    db.session.commit()

    print(f"Applicant {job_applicant_id} successfully applied for job listing {job_listing_id}.")
    return new_application


