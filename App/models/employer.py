from werkzeug.security import check_password_hash, generate_password_hash
from App.database import db
from .user import User

class Employer(User):
    __mapper_args__ = {
        'polymorphic_identity': 'employer',
    }

    id = db.Column(db.Integer, db.ForeignKey('user.id'),primary_key=True)
    created_companies = db.relationship('Company', backref='creator',foreign_keys='Company.creator_id')
    jobListings = db.relationship('JobListing', backref='employer')
    def __init__(self, firstname, lastname, email, username, password):
        super().__init__(firstname, lastname, email, username, password)
    
#     def AttachCompany(self,id):
#         self.company_id = id