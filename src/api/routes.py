"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
from flask import Flask, request, jsonify, url_for, Blueprint
from api.models import db, User
from api.utils import generate_sitemap, APIException
import json
from flask_cors import CORS, cross_origin
from flask_jwt_extended import create_access_token, get_jwt_identity, jwt_required, JWTManager

api = Blueprint('api', __name__)


@api.route('/hello', methods=['POST', 'GET'])
def handle_hello():

    response_body = {
        "message": "Hello! I'm a message that came from the backend, check the network tab on the google inspector and you will see the GET request"
    }

    return jsonify(response_body), 200

@api.route('/sign-up', methods=['POST'])
def handle_register():

    data = request.data
    data_decode = json.loads(data)
    newUser = User(**data_decode)
    user = User.query.filter_by(email=newUser.email,password=newUser.password).first()
    if user is None:
        db.session.add(newUser)
        db.session.commit()
        access_token = create_access_token(identity=newUser.id)
        response_body = {
            "message": "Usuario creado con exito",
            "token":access_token
        }
        return jsonify(response_body), 200
    else :
        response_body = {
            "message": "Usuario ya existe"
        }
        return jsonify(response_body), 400

@api.route('/sign-in', methods=['POST'])
def handle_login():

    data = request.data
    data_decode = json.loads(data)
    user = User.query.filter_by(**data_decode).first()
    if user is None:  
        response_body = {
            "message": "Credenciales Inválidas"
        }
        return jsonify(response_body), 400
    else :
        access_token = create_access_token(identity=user.id)
        response_body = {
            "message": "La logacion con exito",
            "token":access_token
        }
        return jsonify(response_body), 200

@api.route("/privado",methods=["POST"])
@jwt_required()
def handle_private():
    current_user = get_jwt_identity()
    return jsonify(current_user), 200

@api.route("/paginaPrincipal",methods=["POST", "GET"])
@jwt_required()
def handle_userData():
    data = request.data
    data_decode = json.loads(data)
    user = User.query.filter_by(**data_decode).first()
    return jsonify(user_serializado), 200


#     @app.route('/personajes', methods=['GET'])
# def listapersonajes():
#     personajes = Personajes.query.all()
#     personajes_serializado = list(
#     map(lambda personaje: personaje.serialize(), personajes))
#     return jsonify(personajes_serializado), 200