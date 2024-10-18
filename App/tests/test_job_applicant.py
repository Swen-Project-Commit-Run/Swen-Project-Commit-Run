import logging
import unittest
import pytest

from App.controllers.users import get_user
from App.main import create_app
from App.database import db, create_db
from App.models import JobApplicant
from App.controllers import (
    create_job_applicant,
    get_job_listings,
    apply_job,
    CreateJobListing
)
from App.models.applied_for_jobs import AppliedForJobs
from App.models.job_listing import JobListing

LOGGER = logging.getLogger(__name__)

'''
    Unit Tests
'''

class JobApplicantUnitTests(unittest.TestCase):
    def test_create_job_applicant(self):
        applicant = JobApplicant("bob", "doe", "bob@mail.com", "bob52", "bobpass")
        assert applicant.username == "bob52"
        assert applicant.firstname == "bob"
        assert applicant.lastname == "doe"
        assert applicant.email == "bob@mail.com"
        assert applicant.password != "bobpass"  # Password should be hashed
        assert applicant.qualifications == []


    def test_add_qualifications(self):
        applicant = JobApplicant("bob", "doe", "bob@mail.com", "bob52", "bobpass")
        applicant.add_qualifications("Bachelor's Degree", "Master's Degree")
        assert "Bachelor's Degree" in applicant.qualifications
        assert "Master's Degree" in applicant.qualifications

    

'''
Integration Tests
'''

@pytest.fixture(autouse=True, scope="module")
def empty_db():
    app = create_app({'TESTING': True, 'SQLALCHEMY_DATABASE_URI': 'sqlite:///test.db'})
    create_db()
    yield app.test_client()
    db.drop_all()


class JobApplicantIntegrationTests(unittest.TestCase):
    
    

    def test_apply_for_job(self):
        
        applicant = create_job_applicant("jane", "doe", "jane@mail.com", "jane123", "janepass")
        
        job_listing = CreateJobListing(1,"Software Engineer", "Develop and maintain software.")
        
        apply_job(applicant.id, job_listing.id)

        
        application = db.session.query(AppliedForJobs).filter_by(
            applicant_id=applicant.id, job_id=job_listing.id
        ).first()


        # Verify that the application is correctly recorded
        assert application is not None
        assert application.job_id == job_listing.id
        assert application.applicant_id == applicant.id

    def test_get_all_listings(self):
        
        db.session.query(JobListing).delete()
        db.session.commit()
        
        CreateJobListing(2,"Data Scientist", "Analyze data to extract insights.")
        CreateJobListing(3,"Product Manager", "Manage product development.")

       
        listings = get_job_listings()

        
        self.assertEqual(len(listings), 2)  
        
        self.assertIn("Data Scientist", [listing.title for listing in listings])
        self.assertIn("Product Manager", [listing.title for listing in listings])

    def test_add_qualifications(self):
        applicant = create_job_applicant("Jane", "Doe", "jane@mail.com", "JaneDoe", "janepass")
    
        applicant.add_qualifications("Master's Degree in Software Engineering", "5 years of experience in full-stack development")

        retrieved_applicant = get_user(applicant.id)  # Assuming get_user retrieves a user by ID

        expected_qualifications = [
        "Master's Degree in Software Engineering",
        "5 years of experience in full-stack development"
    ]
        assert retrieved_applicant.qualifications == expected_qualifications    
    
        