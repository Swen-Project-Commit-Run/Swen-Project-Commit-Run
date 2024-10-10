from flask import Flask, render_template, request, redirect, flash, jsonify
from flask_jwt_extended import JWTManager, jwt_required, current_user, unset_jwt_cookies, set_access_cookies
from flask_admin import Admin
from App.database import db
from App.models import Employer, JobListing
from App.controllers.job_listing import CreateJobListing, view_applicants_for_jobListing

app= Flask(__name__)
app.config['JWT_SECRET_KEY'] = 'super-secret'  # Change this!
jwt = JWTManager(app)

@app.route('/' , methods=['GET'])
@jwt_required()
def get_job_listings():
    job_listings = JobListing.query.all()
    job_listings_data = [

        {'id': job_listings.id, 'employer_id': job_listings.employer_id, 'title': job_listings.title, 'description': job_listings.description} for job_listings in job_listings
    ]
    return jsonify(job_listings_data), 200
    #return render_template('job_listings.html', job_listings=job_listings)