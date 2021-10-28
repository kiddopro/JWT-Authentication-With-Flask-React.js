"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
from flask import Flask, request, jsonify, url_for, Blueprint
from api.models import db, User
from api.utils import generate_sitemap, APIException

# importación para crear token
from flask_jwt_extended import create_access_token
from flask_jwt_extended import get_jwt_identity
from flask_jwt_extended import jwt_required

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
        return jsonify({"token": access_token, "user_id": user.id, "msg": "user login in correctly" })

# signup
@api.route("/signup", methods=['POST'])
def signup():
    request_body = request.json
    isActive = request_body.get('isActive', True)
    user = User(email=request_body['email'], password=request_body['password'], is_active=isActive)
    db.session.add(user)
    db.session.commit()
    return jsonify({"msg": "User correctly created"}), 200

# private
@api.route('/private', methods=['GET'])
@jwt_required()
def private():
    # Accede a la identidad del usuario actual con get_jwt_identity
    current_user_id = get_jwt_identity()
    user = User.query.get(current_user_id)

    # retornamos los datos del usuario que le pertenece ese token
    return jsonify({"id": user.id, "email": user.email })

# mis endpoints
@api.route('/user', methods=['GET'])
def get_users():
    all_user = User.query.all()
    all_users = list(map(lambda x: x.serialize(), all_user))
    return jsonify(all_users), 200

@api.route('/user/<int:user_id>', methods=['GET'])
def get_user_id(user_id):
    # agarramos la respuesta del json y se la asignamos a body
    body = request.json
    # hacemos una busqueda a User por la id que se le pasa por parametro
    user = User.query.get(user_id)

    # corroboramos que se obtuvo respuesta, de lo contrario no existe un usuario con esa id
    if user is None:
        raise APIException('People not found', status_code=404)
    else:
        return jsonify(user.serialize()), 200



@api.route('/user', methods=['POST'])
def create_user():
    # request_body = request.json # decoded_request = json.loads(request_body)
    # new_user = User.registrar(request_body['email'], request_body['password'])
    # db.session.add(new_user)
    # db.session.commit()

    # obtengo lo que me mandan por json y lo agrego a la base de datos
    request_body = request.json
    is_active = request.json.get('is_active', False)
    user = User(email=request_body['email'], password=request_body['password'], is_active=is_active)
    db.session.add(user)   
    db.session.commit()

    # devuelvo la lista actualizada de usuarios

    all_user = User.query.all()
    all_users = list(map(lambda x: x.serialize(), all_user))

    return jsonify(all_users), 200

@api.route('/user/<int:id_user>', methods=['DELETE'])
def delete_user(id_user):

    # obtenemos el usuario
    user = User.query.get(id_user)

    # verificamos si se encontró un usuario con la id que viene por parametro
    if user is None:
        raise APIException('User not found', status_code=404)
    else:
        # si tiene un favoritos vinculado no puede borrarse
        if user.favorites_planet != [] or user.favorites_people != []:
            raise APIException('User has a relationship with another table', status_code=404)
            
        # si no tiene un favoritos relacionado puede borrarse
        else:
            db.session.delete(user)
            db.session.commit()
            all_user = User.query.all()
            all_users = list(map(lambda x: x.serialize(), all_user))

            return jsonify(all_users), 200



@api.route('/planets', methods=['GET'])
def get_planets():
    all_planet = Planets.query.all()
    all_planets = list(map(lambda x: x.serialize(), all_planet))
    return jsonify(all_planets), 200

@api.route('/planets/<int:planet_id>', methods=['GET'])
def get_planet_id(planet_id):
    # agarramos la respuesta del json y se la asignamos a body
    body = request.json
    # hacemos una busqueda a Planets por la id que se le pasa por parametro
    planet = Planets.query.get(planet_id)

    # corroboramos que se obtuvo respuesta, de lo contrario no existe un planeta con esa id
    if planet is None:
        raise APIException('Planet not found', status_code=404)
    else:
        return jsonify(planet.serialize()), 200

@api.route('/planets', methods=['POST'])
def post_planets():
    # obtengo lo que me mandan por json y lo agrego a la base de datos
    request_body = request.json
    planet = Planets(name=request_body['name'], picture_url=request_body['picture_url'])
    db.session.add(planet)   
    db.session.commit()

    # retorno una lista en json con los datos actualizados

    all_planet = Planets.query.all()
    all_planets = list(map(lambda x: x.serialize(), all_planet))
    return  jsonify(all_planets), 200


@api.route('/planets/<int:id_planet>', methods=['DELETE'])
def delete_planet(id_planet):
    planet = Planets.query.get(id_planet)

    if planet is None:
        raise APIException('Planet not found', status_code=404)
    else:
        # si no tiene un favoritos relacionado puede borrarse
        if planet.favorites_planets == []:
            db.session.delete(planet)
            db.session.commit()
            all_planet = Planets.query.all()
            all_planets = list(map(lambda x: x.serialize(), all_planet))

            return jsonify(all_planets), 200
        # de lo contrario manda un mensaje correspondiente
        else:
            raise APIException('Planet has a relationship with another table', status_code=404)


@api.route('/people', methods=['GET'])
def get_people():
    all_people = People.query.all()
    all_peoples = list(map(lambda x: x.serialize(), all_people))
    return jsonify(all_peoples), 200

@api.route('/people/<int:people_id>', methods=['GET'])
def get_people_id(people_id):
    # agarramos la respuesta del json y se la asignamos a body
    body = request.json
    # hacemos una busqueda a People por la id que se le pasa por parametro
    people = People.query.get(people_id)

    # corroboramos que se obtuvo respuesta, de lo contrario no existe un personaje con esa id
    if people is None:
        raise APIException('People not found', status_code=404)
    else:
        return jsonify(people.serialize()), 200

@api.route('/people', methods=['POST'])
def post_people():
    # obtengo lo que me mandan por json y lo agrego a la base de datos
    request_body = request.json
    people = People(name=request_body['name'], picture_url=request_body['picture_url'])
    db.session.add(people)   
    db.session.commit()

    # retorno una lista en json con los datos actualizados

    all_people = People.query.all()
    all_peoples = list(map(lambda x: x.serialize(), all_people))

    return jsonify(all_peoples), 200

@api.route('/people/<int:id>', methods=['DELETE'])
def delete_people(id):

    people = People.query.get(id)

    if people is None:
        raise APIException('People not found', status_code=404)
    else:
        # si no tiene un favoritos relacionado puede borrarse
        if people.favorites_people == []:
            db.session.delete(people)
            db.session.commit()
            all_people = People.query.all()
            all_peoples = list(map(lambda x: x.serialize(), all_people))

            return jsonify(all_peoples), 200
        # de lo contrario manda un mensaje correspondiente
        else:
            raise APIException('People has a relationship with another table', status_code=404)
            

    

# favorites people/personajes
@api.route('/user/people', methods=['GET'])
def get_favorites_user_people():
    all_favorite = FavoritesPeople.query.all()
    all_favorites = list(map(lambda x: x.serialize(), all_favorite))
    
    return jsonify((all_favorites)), 200

@api.route('/user/people', methods=['POST'])
def post_favorites_user_people():
    # obtengo lo que me mandan por json y lo agrego a la base de datos
    request_body = request.json
    user = User.query.get(request_body['user_id'])
    people = People.query.get(request_body['people_id'])
    if user is None:
        raise APIException('User not found', status_code=404)
    elif people is None:
        raise APIException('People not found', status_code=404)
    else:
        favoritesPeople = FavoritesPeople(user_id=request_body['user_id'], people_id=request_body['people_id'])
        db.session.add(favoritesPeople)   
        db.session.commit()
        
    # retorno una lista en json con los datos actualizados

    all_fav_people = FavoritesPeople.query.all()
    all_fav_peoples = list(map(lambda x: x.serialize(), all_fav_people))

    return jsonify(all_fav_peoples), 200

@api.route('/user/people/<int:id>', methods=['DELETE'])
def del_fav_people(id):
    request_body = request.json # innecesario
    fav = FavoritesPeople.query.get(id)
    if fav is None:
        raise APIException('Identifier for FavoritesPeople is not found', status_code=404)
    else:
        db.session.delete(fav)
        db.session.commit()

    # retornamos nuevamente la lista de favoritos actualizada
    all_fav_people = FavoritesPeople.query.all()
    all_fav_peoples = list(map(lambda x: x.serialize(), all_fav_people))

    return jsonify(all_fav_peoples), 200


# favorites planets
@api.route('/user/planets', methods=['GET'])
def get_favorites_user_planets():

    all_fav = FavoritesPlanets.query.all()
    all_favs = list(map(lambda x: x.serialize(), all_fav))

    return jsonify(all_favs), 200


@api.route('/user/planets', methods=['POST'])
def post_favorites_user_planets():

    # obtengo lo que me mandan por json y lo agrego a la base de datos
    request_body = request.json
    user = User.query.get(request_body['user_id'])
    planet = Planets.query.get(request_body['planet_id'])
    if user is None:
        raise APIException('User not found', status_code=404)
    elif planet is None:
        raise APIException('Planet not found', status_code=404)
    else:
        favoritesPlanet = FavoritesPlanets(user_id=request_body['user_id'], planet_id=request_body['planet_id'])
        db.session.add(favoritesPlanet)   
        db.session.commit()
        
    # retorno una lista en json con los datos actualizados

    all_fav_planet = FavoritesPlanets.query.all()
    all_fav_planets = list(map(lambda x: x.serialize(), all_fav_planet))

    return jsonify(all_fav_planets), 200

@api.route('/user/planets/<int:id>', methods=['DELETE'])
def del_fav_planets(id):
    request_body = request.json # innecesario
    fav = FavoritesPlanets.query.get(id)
    if fav is None:
        raise APIException('Identifier for FavoritesPlanets is not found', status_code=404)
    else:
        db.session.delete(fav)
        db.session.commit()

    # retornamos nuevamente la lista de favoritos actualizada
    all_fav_planet = FavoritesPlanets.query.all()
    all_fav_planets = list(map(lambda x: x.serialize(), all_fav_planet))

    return jsonify(all_fav_planets), 200
