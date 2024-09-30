from werkzeug.security import check_password_hash, generate_password_hash
from App.database import db
from .user import User

class Employer(User):
    __mapper_args__ = {
        'polymorphic_identity': 'employer',
    }

    organization = db.Column(db.String(150), nullable=False)

    def __init__(self, firstName, lastName, email, password, organization):
        super().__init__(firstName, lastName, email, password)
        self.organization = organization

    def get_jason(self):
        data = super().get_json()
        data['organization'] = self.organization
        return data
