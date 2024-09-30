from App.models import JobListing
from App.models import Employer
from App.database import db

def create_listing(title, description, employer_id):
    """Create a job listing as an employer."""
    # Check if the employer exists
    employer = Employer.query.get(employer_id)
    
    if employer is None:
        raise ValueError(f"Employer with ID {employer_id} does not exist.")

    # Create the job listing
    job_listing = JobListing(title=title, description=description, employerId=employer_id)
    db.session.add(job_listing)
    db.session.commit()
    
    return job_listing
    