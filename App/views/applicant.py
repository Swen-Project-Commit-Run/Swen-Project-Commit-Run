from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required  # Import here
from App.controllers.job_applicant import create_job_applicant, apply_job, get_job_listings

applicant_views = Blueprint('applicant_views', __name__)

@applicant_views.route('/applicant/create', methods=['POST'])
@jwt_required()  # Protect this route
def create_applicant_view():
    data = request.json
    applicant = create_job_applicant(
        data.get('firstName'), 
        data.get('lastName'), 
        data.get('email'), 
        data.get('username'), 
        data.get('password')
    )
    
    if applicant:
        return jsonify(applicant.get_json()), 201
    return jsonify({'message': 'Error creating applicant'}), 400

@applicant_views.route('/applicant/apply', methods=['POST'])
@jwt_required()  # Protect this route
def apply_job_view():
    data = request.json
    applicant_id = data.get('applicant_id')
    job_listing_id = data.get('job_listing_id')
    
    applied = apply_job(applicant_id, job_listing_id)
    if applied:
        return jsonify({'message': 'Application successful'}), 201
    return jsonify({'message': 'Error applying for job'}), 400

@applicant_views.route('/job/listings', methods=['GET'])
def get_job_listings_view():
    job_listings = get_job_listings()
    return jsonify([job.get_json() for job in job_listings]), 200
