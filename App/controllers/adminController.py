from App.models import Admin
from App.database import db

def create_admin(username, email, password):
    newuser = Admin(username=username, email=email, password=password)
    db.session.add(newuser)
    db.session.commit()
    return newuser