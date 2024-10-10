from App.database import db
from App.models import Employer,Company


def create_Company(employer_id, companyName):
    employer = Employer.query.get(employer_id)
    if employer is None:
        return None
    newcompany = Company(companyName,employer)
    db.session.add(newcompany)
    db.session.commit(newcompany)
    return Company