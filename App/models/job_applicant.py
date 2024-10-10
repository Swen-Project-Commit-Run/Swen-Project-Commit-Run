from werkzeug.security import check_password_hash, generate_password_hash
from App.database import db
from .user import User

class Job_Applicant(User):
    __tablename__='jobapplicant'
    __mapper_args__ = {
        'polymorphic_identity' : "job_applicant"
    }

    id = db.Column(db.Integer,db.ForeignKey('user.id'),primary_key=True)
    qualificaions = db.Column(db.String(255))
    

    def __init__(self, firstname, lastname, email, username, password):
        super().__init__( firstname, lastname, email, username, password)

    def set_qualifications(self,qualification):
        
        if not isinstance(qualification, str):
            raise TypeError(f"All qualifications must be strings. Invalid type: {type(qualification)}")
        
        self.qualificaions = qualification
    
        

    