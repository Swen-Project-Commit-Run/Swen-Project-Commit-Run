from werkzeug.security import check_password_hash, generate_password_hash
from App.database import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    firstName =  db.Column(db.String(40), nullable=False)
    lastName = db.Column(db.String(40), nullable=False)
    password = db.Column(db.String(120), nullable=False)
    email = db.Column(db.String(50), nullable=False, unique=True)
    role = db.Column(db.String(9), nullable=False)

    __mapper_args__ = {
        'polymorphic_identity': 'User',
        'polymorphic_on': role
        
    }

    def __init__(self, firstName, lastName, email, password):
        self.firstName = firstName
        self.lastName = lastName
        self.set_password(password)
        self.email=email

    def get_json(self):
        return{
            'id': self.id,
            'username': self.username,
            'email' : self.email,
            'role' : self.role
        }

    def set_password(self, password):
        """Create hashed password."""
        self.password = generate_password_hash(password)
    
    def check_password(self, password):
        """Check hashed password."""
        return check_password_hash(self.password, password)

    #maybe add __repr__()
