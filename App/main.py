import os
from flask import Flask, render_template
from flask_uploads import DOCUMENTS, IMAGES, TEXT, UploadSet, configure_uploads
from flask_cors import CORS
from werkzeug.utils import secure_filename
from werkzeug.datastructures import FileStorage

from App.database import init_db
from App.config import load_config

from App.controllers import (
    setup_jwt,
    add_auth_context
)

# Importing the individual view blueprints
# from App.views.auth import auth
from App.views.admin import setup_admin
from App.views.auth_views import auth_views
from App.views.admin_views import admin_views
from App.views.company import company_views
from App.views.listing import listing_views
from App.views.applicant import applicant_views
from App.views.user import user_views
from App.views.index import index_views

def add_views(app):
    # Registering individual blueprints
    app.register_blueprint(auth_views)
    app.register_blueprint(admin_views)
    app.register_blueprint(company_views)
    app.register_blueprint(listing_views)
    app.register_blueprint(applicant_views)
    app.register_blueprint(user_views)
    app.register_blueprint(index_views)

def create_app(overrides={}):
    app = Flask(__name__, static_url_path='/static')
    load_config(app, overrides)
    CORS(app)
    add_auth_context(app)
    
    # Configure file uploads
    photos = UploadSet('photos', TEXT + DOCUMENTS + IMAGES)
    configure_uploads(app, photos)
    
    # Register views/blueprints
    add_views(app)
    
    # Initialize the database
    init_db(app)
    
    # Set up JWT for authentication
    jwt = setup_jwt(app)
    
    # Set up Admin
    setup_admin(app)

    # Handle invalid JWT tokens
    @jwt.invalid_token_loader
    @jwt.unauthorized_loader
    def custom_unauthorized_response(error):
        return render_template('401.html', error=error), 401

    # Push the app context to ensure everything is initialized correctly
    app.app_context().push()

    return app
