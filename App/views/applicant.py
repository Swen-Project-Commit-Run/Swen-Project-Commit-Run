from flask import Flask, request, jsonify
from flask_jwt_extended import JWTManager, jwt_required, create_access_token
from App.database import db
from App.models import Job_Applicant, JobListing, AppliedForJobs
from App.controllers.job_applicant import create_job_applicant, apply_job


app = Flask(__name__)
app.config['JWT_SECRET_KEY'] = 'your_jwt_secret_key'  # Change this to a random secret
jwt = JWTManager(app)

@app.route('/api/register', methods=['POST'])
def register():
    data = request.json
    new_user = create_job_applicant(data['firstName'], data['lastName'], data['email'], data['username'], data['password'])
    if new_user:
        return jsonify({"msg": "User registered successfully"}), 201
    else:
        return jsonify({"msg": "User registration failed"}), 400

@app.route('/api/apply', methods=['POST'])
@jwt_required()
def apply():
    data = request.json
    result = apply_job(data['job_applicant_id'], data['job_listing_id'])
    if result:
        return jsonify({"msg": "Applied to job successfully"}), 200
    else:
        return jsonify({"msg": "Application failed"}), 400

if __name__ == '__main__':
    app.run(debug=True)