from werkzeug.security import check_password_hash, generate_password_hash
from App.database import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username =  db.Column(db.String(40), nullable=False, unique=True)
    password = db.Column(db.String(120), nullable=False)
    email = db.Column(db.String(50), nullable=False, unique=True)

    def __init__(self, username, email, password):
        self.username = username
        self.set_password(password)
        self.email=email

    def get_json(self):
        return{
            'id': self.id,
            'username': self.username,
            'email' : self.email
        }

    def set_password(self, password):
        """Create hashed password."""
        self.password = generate_password_hash(password)
    
    def check_password(self, password):
        """Check hashed password."""
        return check_password_hash(self.password, password)

    #maybe add __repr__()
