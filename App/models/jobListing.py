from App.database import db


class JobListing(db.Model):
    __tablename__ = 'job_listing'
    id= db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(150), nullable=False)
    description = db.Column(db.Text, nullable=False)
    employerId = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    
    job_applications = db.relationship('JobApplication', backref='job_listing', cascade="all, delete", lazy=True)

    def __init__(self, title, description, employerId):
        self.title = title
        self.description = description
        self.employerId = employerId

    def to_json(self):
        return{
            'id': self.id,
            'title': self.title,
            'description': self.description,
            'employer_id' : self.employerId
        }