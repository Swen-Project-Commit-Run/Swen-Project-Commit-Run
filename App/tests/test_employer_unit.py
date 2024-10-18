import unittest

import logging
import unittest
import pytest

from App.controllers.users import get_user
from App.database import db, create_db
from App.database import create_db
from App.main import create_app
from App.models import Employer, JobListing
from App.controllers import (
    create_employer, 
    CreateJobListing, 
    create_job_applicant,
    apply_job,
    get_job_listings,
    remove_listing)

from App.models.applied_for_jobs import AppliedForJobs
from App.models.job_listing import JobListing

LOGGER = logging.getLogger(__name__)

'''
    Unit Tests
'''

class EmployerUnitTests(unittest.TestCase):
    

    def test_create_employer(self):
        # Create a new Employer instance
        new_employer = Employer( "Bob", "Doe", "bobs@mail.com","Bob53", "bobpass")
        
        # Assertions to check if the employer was correctly created
        assert new_employer.username == "Bob53"
        assert new_employer.firstname == "Bob"
        assert new_employer.lastname == "Doe"
        assert new_employer.email == "bobs@mail.com"
        assert new_employer.company == "examplecompany"

    def test_create_job_listing(self):
        # Create an employer instance
        employer = Employer( "Alice", "Smith", "alice@mail.com","Alice54", "alicepass" )
        # Create a new job listing
        new_job_listing = CreateJobListing(employer.id, "Software Engineer", "Job Description")
        
        # Assertions to check if the job listing was correctly created
        assert new_job_listing.title == "Software Engineer"
        assert new_job_listing.description == "Job Description"
        assert new_job_listing.company_id == employer.id

    def test_list_applicants(self):
        # Create a job listing
        job_listing = CreateJobListing(1, "Software Engineer", "Job Description")
        # Simulate applicants applying for the job (this would usually be done with actual applicants)
        job_listing.applicants = ["Applicant1", "Applicant2"]
        
        # Check if the list of applicants is returned correctly
        applicants = job_listing.list_applicants()
        self.assertEqual(len(applicants), 2)
        self.assertIn("Applicant1", applicants)
        self.assertIn("Applicant2", applicants)

    def test_delete_job_listing(self):
        # Create a job listing
        job_listing = CreateJobListing(1, "Product Manager", "Oversee product development.")
        listing_id = job_listing.id

        # Delete the job listing
        remove_listing(listing_id)

        # Verify that the listing was deleted
        deleted_listing = get_job_listings(listing_id)
        assert deleted_listing is None
        
        
'''
integration test
'''       
@pytest.fixture(autouse=True, scope="module")
def empty_db():
    app = create_app({'TESTING': True, 'SQLALCHEMY_DATABASE_URI': 'sqlite:///test.db'})
    create_db()
    yield app.test_client()
    db.drop_all()      


class EmployerIntegrationTests(unittest.TestCase):

    def test_create_job_listing(self):
        # Create an employer
        employer = create_employer( "Jane", "Doe","jane@mail.com", "JaneDoe", "janepass")
        # Create a job listing
        job_listing = CreateJobListing(employer.id, "Software Engineer", "Develop software applications.")

        # Retrieve the job listing
        retrieved_listing = get_job_listings(job_listing.id)

        # Verify that the job listing was created and can be retrieved
        assert retrieved_listing is not None
        assert retrieved_listing.title == "Software Engineer"
        assert retrieved_listing.description == "Develop software applications."
        assert retrieved_listing.company_id == employer.id

    def test_list_applicants(self):
        # Create a job listing
        employer = create_employer( "John", "Smith", "john@mail.com", "JohnSmith", "johnpass")
        job_listing = CreateJobListing(employer.id, "Data Scientist", "Analyze data for insights.")

        # Create job applicants
        applicant1 = create_job_applicant("Alice", "Brown", "alice@mail.com", "alice123", "alicepass")
        applicant2 = create_job_applicant("Bob", "Johnson", "bob@mail.com", "bob123", "bobpass")

        
        apply_job(applicant1.id, job_listing.id)
        apply_job(applicant2.id, job_listing.id)

        applicant_ids = [applicant_id for applicant_id in job_listing.applicants]
        applicants = [get_user(applicant_id) for applicant_id in applicant_ids]

        
        self.assertEqual(len(applicants), 2)
        self.assertIn(applicant1.id, [applicant['id'] for applicant in applicants])
        self.assertIn(applicant2.id, [applicant['id'] for applicant in applicants])
        
    def test_delete_job_listing(self):

        employer = create_employer("MarkTwain", "Mark","mark@mail.com" "Twain", "markpass", )
    
        job_listing = CreateJobListing(employer.id, "Content Writer", "Write engaging content.")
        listing_id = job_listing.id  # Store the ID of the created job listing

        deleted_listing(listing_id)

        deleted_listing = get_job_listings(listing_id)
        assert deleted_listing is None