from flask import Flask, request, jsonify
from flask_jwt_extended import JWTManager, jwt_required, create_access_token
from App.controllers.company import create_Company

app = Flask(__name__)
app.config['JWT_SECRET_KEY'] = 'your_jwt_secret_key'  # Change this to a random secret
jwt = JWTManager(app)

@app.route('/api/create_company', methods=['POST'])
@jwt_required()
def create_company():
    data = request.json
    new_company = create_Company(data['employer_id'], data['companyName'])
    if new_company:
        return jsonify({"msg": "Company created successfully", "company": new_company.name}), 201
    else:
        return jsonify({"msg": "Company creation failed"}), 400

if __name__ == '__main__':
    app.run(debug=True)