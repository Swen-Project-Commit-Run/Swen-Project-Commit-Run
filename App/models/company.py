from App.database import db
from App.models.employer import Employer

class Company(db.Model):
    __tablename__ = 'companies'
    id = db.Column(db.Integer,primary_key=True)
    creator_id = db.Column(db.Integer,db.ForeignKey('user.id'),nullable=False)
    name = db.Column(db.String(100),nullable=True)
    jobListings = db.relationship('JobListing',backref='company',lazy=True)

    def __init__(self, name, creator):
        if not isinstance(creator, Employer):
            raise ValueError("Only an Employer can create a company.")
        self.name = name
        self.creator_id = creator.id