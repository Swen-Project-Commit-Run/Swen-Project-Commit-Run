from App.database import db


class JobListing(db.model):
    __tablename__ = 'job_listings'
    id= db.Column(db.Interger, primary_key=True)
    title = db.Column(db.String(150), nullable=False)
    description = db.Column(db.text, nullable=False)
    employer_id = db.column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    
    employer = db.relationship('Employer', backref='job_listings')

    def __init__(self, title, description, employer_id):
        self.title = title
        self.description = description
        self.employer_id = employer_id

    def to_json(self):
        return{
            'id': self.id,
            'title': self.title,
            'description': self.description,
            'employer_id' : self.employer_id
        }