from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import urllib, json
import config 

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = config.connector
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Data(db.Model):
    __tablename__ = "data"

    _id = db.Column('id', db.Integer, primary_key = True, autoincrement=True)
    _username = db.Column('username', db.String(128))
    _type = db.Column('type', db.String(4))
    _data = db.Column('data', db.JSON)

    def __init__(self, _username = "", _type = "", _data = ""):
        self._username = _username
        self._type = _type
        self._data = _data

    def insert(_username, _type, _data):
        to_insert = Data(_username, _type, _data)
        db.session.add(to_insert)
        db.session.commit()

    def update(_id, _data):
        to_update = Data.query.filter_by(_id = _id).first()
        to_update._id = _data
        db.session.commit()

    def delete(idd):
        to_delete = Data.session.query.filter_by(_id = _id).first()
        db.session.delete(to_delete)
        db.session.commit()

    def select(idd):
        to_select = Data.query.filter_by(_id = _id).first()
        return to_select._data


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

    def delete(_id):
        to_delete = Users.session.query.filter_by(_id = _id).first()
        db.session.delete(to_delete)
        db.session.commit()

    def select(_id):
        to_select = Users.query.filter_by(_id = _id).first()
        return to_select._username
