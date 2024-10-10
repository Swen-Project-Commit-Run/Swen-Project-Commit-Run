from App.database import db

class JobListing(db.Model):
    __tablename__ = 'job_listing'
    
    id = db.Column(db.Integer, primary_key=True)
    employer_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    company_id = db.Column(db.Integer, db.ForeignKey('company.id'), nullable=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(255), nullable=False)

    employer = db.relationship('Employer', backref='job_listings')
    company = db.relationship('Company', backref='job_listings',cascade="all, delete", lazy=True)
    job_applications = db.relationship('AppliedForJobs', backref='job_listing', cascade="all, delete", lazy=True)

    def __init__(self, employer_id, title, description, company_id=None):
        self.employer_id = employer_id
        self.title = title
        self.description = description
        self.company_id = company_id  # Optional: can be None if not provided

    def list_applicants(self):
        return self.applicants
