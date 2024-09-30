from werkzeug.security import check_password_hash, generate_password_hash
from App.database import db
from .user import User

class Employer(User):
    __mapper_args__ = {
        'polymorphic_identity': 'employer',
    }

    organization = db.Column(db.String(150), nullable=False)

    def __init__(self, username, email, password, organization):
        super().__init__(username, email, password)
        self.organization = organization

    #maybe do json