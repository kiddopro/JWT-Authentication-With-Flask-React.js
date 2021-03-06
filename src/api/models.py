from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=False, nullable=False)
    is_active = db.Column(db.Boolean(), unique=False, nullable=False)
    favorites_people = db.relationship('FavoritesPeople', backref="user")
    favorites_planet = db.relationship('FavoritesPlanets', backref="user")

    def __repr__(self):
        return '<User %r>' % self.email

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            # do not serialize the password, its a security breach
        }

class Planets(db.Model):
    __tablename__ = 'planets'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(150), unique=True, nullable=False)
    picture_url = db.Column(db.String(250))
    favorites_planets = db.relationship('FavoritesPlanets', backref="planets")

    def __repr__(self):
        return '<Planets %r>' % self.name

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "picture_url": self.picture_url
        }

class People(db.Model):
    __tablename__ = 'people'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(150), unique=True, nullable=False)
    picture_url = db.Column(db.String(250))
    favorites_people = db.relationship('FavoritesPeople', backref="people")

    def __repr__(self):
        return '<People %r>' % self.name

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "picture_url": self.picture_url,
            # "favorites_people": list(map(lambda x: x.serialize(), self.favorites_people))
        }


class FavoritesPeople(db.Model):
    # __tablename__ = 'favoritespeople'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    people_id = db.Column(db.Integer, db.ForeignKey('people.id'), nullable=False)
    # user = db.relationship(User)
    # people = db.relationship(People)

    def __repr__(self):
        return '<FavoritesPeople %r>' % self.id

    def serialize(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "people_id": self.people_id
        }



class FavoritesPlanets(db.Model):
    # __tablename__ = 'favoritespeople'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    planet_id = db.Column(db.Integer, db.ForeignKey('planets.id'), nullable=False)
    # user = db.relationship(User)
    # people = db.relationship(People)

    def __repr__(self):
        return '<FavoritesPlanets %r>' % self.id

    def serialize(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "planet_id": self.planet_id
        }