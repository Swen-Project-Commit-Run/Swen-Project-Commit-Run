from App.database import db

class JobApplication(db.Model):
    __tablename__='Job_Applications'
    id=db.Column(db.Integer, primary_key=True)
    jobId =db.Column(db.Integer, db.ForeignKey('job_listing.id'), nullable=False)
    applicantId = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    jobListing = db.relationship('JobListing', backref='jobApplications')
    applicant = db.relationship('Applicant', backref='applicantApplication')

    def __init__(self, jobId, applicantId):
        self.jobId = jobId
        self.applicantId = applicantID

    def to_json(self):
        return{
            'id': self.id,
            'job_id': self.jobId,
            'applicant_id': self.applicant_id
        }