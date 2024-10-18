from App.controllers import job_applicant
from App.database import db
from App.models import JobListing,Employer, AppliedForJobs
from App.models.user import User


def CreateJobListing(employee_id, title, description):
    employer = Employer.query.get(employee_id)
    if employer is None:
        raise ValueError(f"Employer with ID {employee_id} does not exist.")
    jobListing = JobListing(employer.id, title, description)
    db.session.add(jobListing)
    db.session.commit()  # Commit the session first
    return jobListing  


def view_applicants_for_jobListing(jobListing_id):
    # Fetch the job listing using the provided ID
    job_listing = JobListing.query.get(jobListing_id)

    if not job_listing:
        print(f"Job listing with ID {jobListing_id} not found.")
        return

    # Fetch all applications for the job listing using the model
    job_applications = AppliedForJobs.query.filter_by(job_id=jobListing_id).all()

    if not job_applications:
        print(f"No applicants for job listing ID {jobListing_id}.")
        return

    # Fetch applicant details for each job application
    for application in job_applications:
        applicant = User.query.get(application.applicant_id)  
        if applicant:
            print(f"Applicant ID: {applicant.id}, Name: {applicant.firstname} {applicant.lastname}")
        else:
            print(f"Applicant with ID {application.applicant_id} not found.")

    return job_applications




