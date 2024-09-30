from werkzeug.security import check_password_hash, generate_password_hash
from App.database import db
from .user import User

class Applicant(User):
    __mapper_args__ = {
        'polymorphic_identity' : "job_applicant"
    }

    def __init__(self, username, email, password):
        super().__init__(username, email, password)
        

    