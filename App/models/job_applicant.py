from werkzeug.security import check_password_hash, generate_password_hash
from App.database import db
from .user import User
from sqlalchemy.dialects.postgresql import JSON

class Job_Applicant(User):
    __tablename__='jobapplicant'
    __mapper_args__ = {
        'polymorphic_identity': "job_applicant"
    }

    id = db.Column(db.Integer, db.ForeignKey('user.id'), primary_key=True)
    qualifications = db.Column(JSON)
    applied_for_jobs = db.relationship(
        'JobListing',
        secondary='applied_for_job',
        backref=db.backref('applicants', lazy=True, cascade='all, delete'),
    )


    def __init__(self, firstname, lastname, email, username, password):
        super().__init__(firstname, lastname, email, username, password)
        self.qualifications = []

    def add_qualifications(self, *qualifications):
        if not qualifications:
            raise ValueError("You must provide at least one qualification.")
        self.qualifications.extend(qualifications)