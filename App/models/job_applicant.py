from werkzeug.security import check_password_hash, generate_password_hash
from App.database import db
from .user import User

class Job_Applicant(User):
    __mapper_args__ = {
        'polymorphic_identity' : "job_applicant"
    }

    id = db.Column(db.Integer,db.ForeignKey('user.id'),primary_key=True)
    qualificaions = db.Column(db.ARRAY(db.String))
    applied_for_jobs = db.relationship('JobListing',secondary='applied_for_job',backref=db.backref('applicants',lazy=True))

    def __init__(self, firstname, lastname, email, username, password):
        super().__init__( firstname, lastname, email, username, password)

    def add_qualifications(self,*qualifications):
        if not qualifications:
            raise ValueError("You must provide at least one qualification.")
        
        for qualification in qualifications:
            if not isinstance(qualification, str):
                raise TypeError(f"All qualifications must be strings. Invalid type: {type(qualification)}")

        self.qualificaions = qualifications
    
        

    