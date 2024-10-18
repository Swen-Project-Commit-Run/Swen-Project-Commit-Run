from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required  # Import here
from App.controllers.adminController import create_admin, remove_user, remove_listing

admin_views = Blueprint('admin_views', __name__)

@admin_views.route('/admin/create', methods=['POST'])
@jwt_required()  # Protect this route
def create_admin_view():
    data = request.json
    admin = create_admin(
        data.get('firstName'), 
        data.get('lastName'), 
        data.get('email'), 
        data.get('username'), 
        data.get('password')
    )
    
    if admin:
        return jsonify(admin.get_json()), 201
    return jsonify({'message': 'Error creating admin'}), 400

@admin_views.route('/admin/remove_user/<int:user_id>', methods=['DELETE'])
@jwt_required()  # Protect this route
def remove_user_view(user_id):
    remove_user(user_id)
    return jsonify({'message': f'User {user_id} removed.'}), 200

@admin_views.route('/admin/remove_listing/<int:listing_id>', methods=['DELETE'])
@jwt_required()  # Protect this route
def remove_listing_view(listing_id):
    remove_listing(listing_id)
    return jsonify({'message': f'Job listing {listing_id} removed.'}), 200
