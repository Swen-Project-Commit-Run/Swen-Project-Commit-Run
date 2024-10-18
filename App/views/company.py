from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required  # Import here
from App.controllers.company import create_Company, list_CompanyJobLisings

company_views = Blueprint('company_views', __name__)

@company_views.route('/company/create', methods=['POST'])
@jwt_required()  # Protect this route
def create_company_view():
    data = request.json
    company = create_Company(data.get('employer_id'), data.get('companyName'))
    
    if company:
        return jsonify(company.get_json()), 201
    return jsonify({'message': 'Error creating company'}), 400

@company_views.route('/company/jobs/<string:company_name>', methods=['GET'])
def list_company_jobs_view(company_name):
    jobs = list_CompanyJobLisings(company_name)
    if jobs is None:
        return jsonify({'message': 'Company not found'}), 404
    return jsonify([job.get_json() for job in jobs]), 200
