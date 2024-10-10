from App.models import Admin
from App.models import User
from App.models import JobListing
from App.database import db

def create_admin(firstName, lastName, email,username, password):
    newuser = Admin(firstName, lastName, email,username, password)
    db.session.add(newuser)
    db.session.commit()
    return newuser

def remove_user(user_id):
    """Remove a user (either an Employer or an Applicant)."""
    user = User.query.get(user_id)
    
    if user:
        db.session.delete(user)
        db.session.commit()
        print(f"User {user_id} removed.")
    else:
        print(f"User {user_id} not found.")

def remove_listing(listing_id):
    job_listing = JobListing.query.get(listing_id)
    
    if job_listing:
        db.session.delete(job_listing)
        db.session.commit()
        print(f"Job listing {listing_id} and associated job applications removed.")
    else:
        print(f"Job listing {listing_id} not found.")
