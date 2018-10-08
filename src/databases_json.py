import json

with open('./src/json/row_user.json') as f:
    user_json = json.load(f)

with open('./src/json/row_data.json') as f:
    data_json = json.load(f)

users = []
data = []

class Data():
    def __init__(self, _username = "", _type = "", _data = ""):
        self._username = _username
        self._type = _type
        self._data = _data

    def insert(_username, _type, _data):
        data_json["username"] = _username
        data_json["type"] = _type
        data_json["data"] = _data
        data.append({"username": _username,"type": _type,"data": _data})

    def updateData(_username, _type, _data):
        for x in data:
            if x["username"] == _username and x["type"] == _type:
                x["data"] = _data
                return True

        return False

    def delete(_username, _type):
        for i in range(len(data)):
            if data[i]["username"] == _username and data[i]["type"] == _type:
                data.pop(i)
                return True

        return False

    def exist(_username, _type):
        for x in data:
            if x["username"] == _username and x["type"] == _type:
                return True
        
        return False

    def getData(_username, _type):
        for x in data:
            if x["username"] == _username and x["type"] == _type:
                return x["data"]

    def tableSize():
        return len(data)

    def _dropTable():
        for x in range(len(data)):
            data.pop(x)
        


class Users():
    def __init__(self, _username = ""):
        self._username = _username

    def insert(_username):
        users.append(_username)

    def delete(_username):
        for i in range(len(users)):
            if users[i] == _username:
                users.pop(i)
                return True

        return False

    def exist(_username):
        for x in users:
            if x == _username:
                return True
        
        return False

    def tableSize():
        return len(users)

    def _dropTable():
        for x in range(len(users)):
            users.pop(x)