from App.models import Employer
from App.models import JobListing
from App.models import JobApplication
from App.models import Applicant
from App.database import db

def create_employer(firstName, lastName, email, password):
    newuser = Employer(firstName=firstName, lastName=lastName, email=email, password=password)
    db.session.add(newuser)
    db.session.commit()
    return newuser

def view_applicants_for_employer(employer_id):
    #View all applicants who applied for jobs created by the given employer.
    employer = Employer.query.get(employer_id)
    
    if not employer:
        print(f"Employer with ID {employer_id} not found.")
        return

    job_listings = JobListing.query.filter_by(employerId=employer_id).all()

    if not job_listings:
        print(f"No job listings found for Employer ID {employer_id}.")
        return
    
    # Iterate through each job listing created by the employer
    for job in job_listings:
        print(f"\nApplicants for Job: {job.title} (ID: {job.id})")
        
        job_applications = JobApplication.query.filter_by(jobId=job.id).all()

        if not job_applications:
            print(f"No applicants for this job.")
            continue
        
        # Fetch and display applicants for each job
        for application in job_applications:
            applicant = Applicant.query.get(application.applicantId)
            if applicant:
                print(f"{applicant.firstName} {applicant.lastName} with email: {applicant.email} applied for {job.title}")

    
def view_applicants_for_job(job_id):
    #View all applicants who applied for the job with the given job ID.
    # Fetch the job listing using the job_id
    job_listing = JobListing.query.get(job_id)
    
    if not job_listing:
        print(f"Job listing with ID {job_id} not found.")
        return

    # Fetch all applications for the job listing
    job_applications = JobApplication.query.filter_by(jobId=job_id).all()

    if not job_applications:
        print(f"No applicants for job listing ID {job_id}.")
        return
    
    print(f"\nApplicants for Job: {job_listing.title} (ID: {job_listing.id})")
    
    # Iterate through applications and display applicant information
    for application in job_applications:
        applicant = Applicant.query.get(application.applicantId)
        if applicant:
            print(f"{applicant.firstName} {applicant.lastName} with email {applicant.email} applied for {job_listing.title}")
