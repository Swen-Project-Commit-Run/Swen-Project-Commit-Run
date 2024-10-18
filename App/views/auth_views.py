from flask import Blueprint, request, jsonify
from App.controllers.auth import login

auth_views = Blueprint('auth_views', __name__)

@auth_views.route('/login', methods=['POST'])
def login_view():
    data = request.json
    username = data.get('username')
    password = data.get('password')
    token = login(username, password)
    
    if token:
        return jsonify({'token': token}), 200
    return jsonify({'message': 'Invalid credentials'}), 401
