from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required  # Import here
from App.controllers.users import create_user, get_user, get_all_users_json

user_views = Blueprint('user_views', __name__)

@user_views.route('/user/create', methods=['POST'])
@jwt_required()  # Protect this route
def create_user_view():
    data = request.json
    user = create_user(
        data.get('firstName'), 
        data.get('lastName'), 
        data.get('email'), 
        data.get('username'), 
        data.get('password')
    )
    
    if user:
        return jsonify(user.get_json()), 201
    return jsonify({'message': 'Error creating user'}), 400

@user_views.route('/user/<int:user_id>', methods=['GET'])
@jwt_required()  # Protect this route
def get_user_view(user_id):
    user = get_user(user_id)
    if user:
        return jsonify(user.get_json()), 200
    return jsonify({'message': 'User not found'}), 404

@user_views.route('/users', methods=['GET'])
@jwt_required()  # Protect this route
def get_all_users_view():
    users = get_all_users_json()
    return jsonify(users), 200
