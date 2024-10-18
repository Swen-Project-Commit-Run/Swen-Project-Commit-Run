from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required  # Import here
from App.controllers.job_listing import CreateJobListing, view_applicants_for_jobListing

listing_views = Blueprint('listing_views', __name__)

@listing_views.route('/job/create', methods=['POST'])
@jwt_required()  # Protect this route
def create_job_listing_view():
    data = request.json
    try:
        job = CreateJobListing(data.get('employer_id'), data.get('title'), data.get('description'))
        return jsonify(job.get_json()), 201
    except ValueError as e:
        return jsonify({'message': str(e)}), 400

@listing_views.route('/job/applicants/<int:job_listing_id>', methods=['GET'])
def view_applicants_for_job_listing_view(job_listing_id):
    try:
        applicants = view_applicants_for_jobListing(job_listing_id)
        return jsonify([applicant.get_json() for applicant in applicants]), 200
    except ValueError as e:
        return jsonify({'message': str(e)}), 404
