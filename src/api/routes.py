"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
from flask import Flask, request, jsonify, url_for, Blueprint
from api.models import db, User
from api.utils import generate_sitemap, APIException

# importación para crear token
from flask_jwt_extended import create_access_token
from flask_jwt_extended import get_jwt_identity

api = Blueprint('api', __name__)


# login
@api.route("/login", methods=["POST"])
def login():
    email = request.json.get("email", None)
    password = request.json.get("password", None)

    # filtramos los usuarios segun su email y contraseña
    user = User.query.filter_by(email=email, password=password).first()

    # si no encuentra match en la base de datos retorna el mensaje correspondiente
    if user is None:
        return jsonify({"msg": "Bad email or password"}), 401
    else:
        # de lo contrario se crea un token haciendo referencia a la id del usuario
        access_token = create_access_token(identity=user.id)
        # retornamos un json con los datos del token y la id de usuario a la que se le esta asignando el mismo
        return jsonify({"token": access_token, "user_id": user.id })

# signup
@api.route("/signup", methods=['POST'])
def signup():
    request_body = request.json
    isActive = request_body.get('isActive', True)
    user = User(email=request_body['email'], password=request_body['password'], is_active=isActive)
    db.session.add(user)
    db.session.commit()
    return jsonify({"msg": "User created"}), 200

# private
@api.route('/private', methods=['GET'])
@jwt_required()
def private():
    # Accede a la identidad del usuario actual con get_jwt_identity
    current_user_id = get_jwt_identity()
    user = User.filter.get(current_user_id)

    # retornamos los datos del usuario que le pertenece ese token
    return jsonify({"id": user.id, "username": user.username })