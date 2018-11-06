from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import urllib, json
import os

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['MYSQL_KEY']
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///ipc.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class APIUsers(db.Model):
    __tablename__ = "apiusers"

    _id = db.Column('id', db.Integer, primary_key = True, autoincrement=True)
    _public_id = db.Column('public_id', db.String(50))
    _name = db.Column('name', db.String(50))
    _password = db.Column('password', db.String(100))
    _admin = db.Column('admin', db.Boolean)

    def __init__(self, _public_id = "", _name = "", _password = "", _admin=False):
        self._public_id = _public_id
        self._name = _name
        self._password = _password
        self._admin = _admin

    def existsUserByName(_name):
        return APIUsers.query.filter_by(_name = _name).count() == 1

    def existsUserByPublicID(_public_id):
        return APIUsers.query.filter_by(_public_id = _public_id).count() == 1

    def addUser(_public_id, _name, _password, _admin):
        to_insert = APIUsers(_public_id, _name, _password, _admin)
        db.session.add(to_insert)
        db.session.commit()

    def getAllUsers():
        # Se devuelve una lista con todos los usuarios
        return APIUsers.query.all()

    def getUserByPublicID(_public_id):
        return APIUsers.query.filter_by(_public_id = _public_id).first()

    def getUserByName(_name):
        return APIUsers.query.filter_by(_name = _name).first()

    def deleteUser(_public_id):
        to_delete = APIUsers.query.filter_by(_public_id = _public_id).first()
        db.session.delete(to_delete)
        db.session.commit()
        

class Data(db.Model):
    __tablename__ = "data"

    _id = db.Column('id', db.Integer, primary_key = True, autoincrement=True)
    _username = db.Column('username', db.String(128))
    _type = db.Column('type', db.String(4))
    _data = db.Column('data', db.String(1000))

    def __init__(self, _username = "", _type = "", _data = {'data':[]}):
        self._username = _username
        self._type = _type
        self._data = json.dumps(_data)

    def createNetwork(_username, _type):
        to_insert = Data(_username, _type)
        db.session.add(to_insert)
        db.session.commit()

    def updateData(_username, _type, _data):
        to_update = Data.query.filter_by(_username = _username, _type = _type).first()
        to_update._data = json.dumps(_data)
        db.session.commit()

    def getData(_username, _type):
        to_get = Data.query.filter_by(_username = _username, _type = _type).first()
        return json.loads(to_get._data)

    def getAllData(_username):
        to_get = Data.query.filter_by(_username = _username).all()
        # to_get es una lista que contiene todas las redes de _username
        return to_get

    def countType(_type):
        to_get = Data.query.filter_by(_type = _type).all()
        return len(to_get)

    def delete(_username, _type):
        to_delete = Data.query.filter_by(_username = _username, _type = _type).first()
        db.session.delete(to_delete)
        db.session.commit()

    def exist(_username, _type):
        return Data.query.filter_by(_username = _username, _type = _type).count() == 1

    def tableSize():
        return Data.query.filter_by().count()

    def _dropTable():
        for nr in db.session.query(Data._id).distinct():
            row_to_delete = Data.query.get(nr)
            test = row_to_delete._username
            db.session.delete(row_to_delete)

        db.session.commit()
        


class Users(db.Model):
    __tablename__ = "users"

    _id = db.Column('id', db.Integer, primary_key = True, autoincrement=True)
    _username = db.Column('username', db.String(128))

    def __init__(self, _username = ""):
        self._username = _username

    def insert(_username):
        to_insert = Users(_username)
        db.session.add(to_insert)
        db.session.commit()

    def update(_id, _username):
        to_update = Users.query.filter_by(_id = _id).first()
        to_update._username = _username
        db.session.commit()

    def delete(_username):
        to_delete = Users.query.filter_by(_username = _username).first()
        db.session.delete(to_delete)
        db.session.commit()

    def exist(_username):
        return Users.query.filter_by(_username = _username).count() == 1

    def tableSize():
        return Users.query.filter_by().count()

    def _dropTable():
        for nr in db.session.query(Users._id).distinct():
            row_to_delete = Users.query.get(nr)
            test = row_to_delete._username
            db.session.delete(row_to_delete)

        db.session.commit()