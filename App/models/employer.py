# from werkzeug.security import check_password_hash, generate_password_hash
# from App.database import db
# from .user import User

# class Employer(User):
#     __mapper_args__ = {
#         'polymorphic_identity': 'employer',
#     }

#     id = db.Column(db.Integer, db.ForeignKey('user.id'),primary_key=True)
#     #company_id = db.Column(db.Integer,db.ForeignKey('company.id'))
#     company_name = db.Column(db.String(50), nullable=False)
#     def __init__(self, firstname, lastname, email, username, password):
#         super().__init__(firstname, lastname, email, username, password)
    
#     def AttachCompany(self,id):
#         self.company_id = id