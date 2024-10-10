from App.database import db

class AppliedForJobs(db.Model):
    __tablename__ = 'applied_for_job'
    
    id = db.Column(db.Integer, primary_key=True)
    job_id = db.Column(db.Integer, db.ForeignKey('job_listing.id'), nullable=False)
    applicant_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    
    def __init__(self,job_id,applicant_id):
        self.job_id = job_id
        self.applicant_id = applicant_id