from werkzeug.security import check_password_hash, generate_password_hash
from App.database import db

class User(db.Model):
        id = db.Column(db.Integer,primary_key= True)
        email = db.Column(db.String(120),unique=True, nullable=False)
        firstname = db.Column(db.String(50), nullable=False)
        lastname = db.Column(db.String(50),nullable=False)
        username = db.Column(db.String(50),unique=True,nullable=False)
        password = db.Column(db.String(128),nullable = False)

        type = db.Column(db.String(50))
        
        __mapper_args__ = {
            'polymorphic_on': type
            }

        def __init__(self, firstname, lastname, email, username, password):
            self.firstname = firstname
            self.lastname = lastname
            self.email = email
            self.username = username
            self.set_password(password)  # Hash and set the password
    
        def set_password(self,password):
            self.password = generate_password_hash(password)
   
    
        def check_password(self, password):
            return check_password_hash(self.password,password)
        
        def get_json(self):
             return {
                  'id': self.id,
                  'firstname': self.firstname,
                  'lastname': self.lastname,
                  'email': self.email,
                  'username': self.username,
                  'password': self.password
             }
        
