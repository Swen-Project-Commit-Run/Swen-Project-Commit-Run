import unittest

import logging
import unittest
import pytest

from App.controllers.job_listing import CreateJobListing
from App.controllers.users import create_user, get_user
from App.database import db, create_db
from App.database import create_db
from App.main import create_app
from App.models import Admin
from App.controllers import (
    remove_user)

class AdminUnitTests(unittest.TestCase):

    def test_create_admin(self):
        # Create an admin instance
        new_admin = Admin("John", "Smith", "john@mail.com", "johnadmin", "adminpass")
        
        # Verify the attributes of the new admin
        assert new_admin.first_name == "John"
        assert new_admin.last_name == "Smith"
        assert new_admin.email == "john@mail.com"
        assert new_admin.username == "johnadmin"
        assert new_admin.password == "adminpass"
        assert new_admin.type == "admin"  # Ensure admin type is set correctly

    def test_delete_user(self):
        user_id = 1  # Assuming you have a user with ID 1 to test deletion
        remove_user(user_id)
        
        # Verify that the user is deleted
        assert get_user(user_id) is None
        
'''
integration test
'''       
@pytest.fixture(autouse=True, scope="module")
def empty_db():
    app = create_app({'TESTING': True, 'SQLALCHEMY_DATABASE_URI': 'sqlite:///test.db'})
    create_db()
    yield app.test_client()
    db.drop_all() 
    
class AdminIntegrationTests(unittest.TestCase):

    def test_delete_user(self):
        # Create a user to be deleted
        user = create_user("tempuser", "temppassword")
        user_id = user.id  # Get the ID of the created user

        # Delete the user
        remove_user(user_id)

        # Verify the user cannot be retrieved
        assert get_user(user_id) is None
