from .databases import Users, Data, APIUsers
import json, simplejson, ipaddress
from flask import jsonify
import uuid, jwt, datetime, os
from werkzeug.security import generate_password_hash, check_password_hash

def mergeJSON(jsonA, jsonB):
    # for i in range(len(jsonB["data"])):
    #     jsonA["data"].append(jsonB["data"][int(i)])
    jsonA["data"].append(jsonB)

    return jsonA

class IPContainer():

    def existUser(_username):
        return Users.exist(_username)

    def addUser(_username):
        ret = False
        if not Users.exist(_username):
            Users.insert(_username)
            ret = True

        return ret

    def removeUser(_username):
        ret = False
        if Users.exist(_username):
            Users.delete(_username)
            ret = True

        return ret

    def getNumberOfUsers():
        return Users.tableSize()

    def getNumberOfNetworks():
        return Data.tableSize()

    def existNetwork(_username, _type):
        return Data.exist(_username, _type)

    def createNetwork(_username, _type):
        ret = False
        if Users.exist(_username):
            if not Data.exist(_username, _type):
                Data.createNetwork(_username, _type)
                ret = True

        return ret

    def removeNetwork(_username, _type):
        ret = False
        if Users.exist(_username):
            if Data.exist(_username, _type):
                Data.delete(_username, _type)
                ret = True

        return ret

    def addIPtoNetwork(_username, _type, _data):
        ret = False
        if Users.exist(_username):
            if Data.exist(_username, _type):
                jsonA = Data.getData(_username, _type)
                jsonMerged = mergeJSON(jsonA, _data)
                Data.updateData(_username, _type, jsonMerged)
                ret = True

        return ret

    def removeIPfromNetwork(_username, _type, _ip):
        ret = False
        if Users.exist(_username):
            if Data.exist(_username, _type):
                data = Data.getData(_username, _type)

                if _type == "dns":
                    for i in range(len(data["data"]) - 1):
                        print(len(data["data"]))
                        if data["data"][int(i)]["dns1"] == _ip or data["data"][int(i)]["dns2"] == _ip:
                            data["data"].pop(int(i))
                            ret = True

                else:
                    for i in range(len(data["data"]) - 1):
                        if data["data"][int(i)]["ip"] == _ip:
                            data["data"].pop(int(i))
                            ret = True

                if ret:
                    Data.updateData(_username, _type, data)

        return ret

    def getNetworkSize(_username, _type):
        if Users.exist(_username):
            if Data.exist(_username, _type):
                return len(Data.getData(_username, _type)["data"])

        return None

    def getData(_username, _type):
        if Users.exist(_username):
            if Data.exist(_username, _type):
                return Data.getData(_username, _type)

        return None

    def getAllData(_username):
        djson = {'username':_username, 'noofnetworks':0, 'networks':[]}
        if Users.exist(_username):
            data = Data.getAllData(_username)
            djson['noofnetworks'] = len(data)
            for i in range (len(data)):
                djson['networks'].append({'type':data[i]._type, 'network':data[i]._data})

        return json.dumps(djson)

    def getStatus():
        networks = {'dns':Data.countType('dns'), 'wlan':Data.countType('wlan'), 'vlan':Data.countType('vlan'), 'pan':Data.countType('pan'), 'lan':Data.countType('lan'), 'wan':Data.countType('wan'), 'san':Data.countType('san')}
        
        return jsonify(status='OK', noofusers=IPContainer.getNumberOfUsers(), noofnetworks=IPContainer.getNumberOfNetworks(), networks=networks)

    def _dropUsers():
        Users._dropTable()

    def _dropData():
        Data._dropTable()

    #############################
    #   Token authentication    #
    #############################
    def addAPIUser(_user, _password):
        ret = False
        if not APIUsers.existsUserByName(_user):
            hashed_passwd = generate_password_hash(_password, method='sha256')
            APIUsers.addUser(str(uuid.uuid4()), _user, hashed_passwd)
            ret = True

        return ret

    def getAllAPIUsers():
        users = APIUsers.getAllUsers()
        output = []

        for user in users:
            user_data = {'public_id':user._public_id, 'username':user._name, 'password':user._password}
            output.append(user_data)

        return jsonify(apiusers=output, noofusers=len(output))

    def getAPIUser(_public_id):
        user = APIUsers.getUserByPublicID(_public_id)

        if not user:
            return jsonify(message="No user found.")
        
        user_data = {'public_id':user._public_id, 'username':user._name, 'password':user._password}

        return jsonify(user=user_data)

    def deleteAPIUser(_public_id):
        if not APIUsers.existsUserByPublicID(_public_id):
            return jsonify(message="No user found.")

        APIUsers.deleteUser(_public_id)

        return jsonify(message="User deleted.")

    def login(username, password):
        if not APIUsers.existsUserByName(username):
            return jsonify(message="No user found.")

        user = APIUsers.getUserByName(username)

        if check_password_hash(user._password, password):
            token = jwt.encode({'public_id' : user._public_id, 'exp' : datetime.datetime.utcnow() + datetime.timedelta(minutes=20)}, os.environ['SECRET_KEY'])
            return jsonify(token=token.decode('UTF-8'))

        return jsonify(message="Could not verify.")

    def tokenAccess(token):
        try:
            data = jwt.decode(token, os.environ['SECRET_KEY'])
            return APIUsers.getUserByPublicID(data['public_id'])
        except:
            return None