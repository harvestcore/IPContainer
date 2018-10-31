import json
from flask import Flask, jsonify, request, make_response
from src.ipcontainer import IPContainer
from functools import wraps

app = Flask(__name__)

def token_requiered(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None

        if 'x-access-token' in request.headers:
            token = request.headers['x-access-token']

        if not token:
            return jsonify(message="Token is missing."), 401

        current_user = IPContainer.tokenAccess(str(token))

        if not current_user:
            return jsonify(message="Token is invalid."), 401

        return f(current_user, *args, **kwargs)

    return decorated            


@app.route("/", methods=['GET'])
def index():
    return jsonify(status='OK')

@app.route("/status", methods=['GET'])
def status():
    return IPContainer.getStatus()

@app.route("/addUser/<user>", methods=['POST'])
@token_requiered
def addUser(current_user, user):
    return jsonify(success=IPContainer.addUser(str(user)))

@app.route("/removeUser/<user>", methods=['DELETE'])
@token_requiered
def removeUser(current_user, user):
    return jsonify(success=IPContainer.removeUser(str(user)))

@app.route("/getNumberOfUsers", methods=['GET'])
@token_requiered
def getNumberOfUsers(current_user):
    return jsonify(users=IPContainer.getNumberOfUsers())

@app.route("/existsUser/<user>", methods=['GET'])
@token_requiered
def existUser(current_user, user):
    return jsonify(exists=IPContainer.existUser(str(user)))

@app.route("/getNumberOfNetworks", methods=['GET'])
@token_requiered
def getNumberOfNetworks(current_user):
    return jsonify(networks=IPContainer.getNumberOfNetworks())

@app.route("/existsNetwork/<user>/<_type>", methods=['GET'])
@token_requiered
def existNetwork(current_user, user, _type):
    return jsonify(exists=IPContainer.existNetwork(str(user), str(_type)))

@app.route("/createNetwork/<user>/<_type>", methods=['POST'])
@token_requiered
def createNetwork(current_user, user, _type):
    return jsonify(success=IPContainer.createNetwork(str(user), str(_type)))

@app.route("/removeNetwork/<user>/<_type>", methods=['DELETE'])
@token_requiered
def removeNetwork(current_user, user, _type):
    return jsonify(success=IPContainer.removeNetwork(str(user), str(_type)))

@app.route("/addIPtoNetwork/<user>/<_type>/<ip>", methods=['POST'])
@token_requiered
def addIPtoNetwork(current_user, user, _type, ip):
    return jsonify(success=IPContainer.addIPtoNetwork(str(user), str(_type), str(ip)))
    
@app.route("/removeIPfromNetwork/<user>/<_type>/<ip>", methods=['DELETE'])
@token_requiered
def removeIPfromNetwork(current_user, user, _type, ip):
    return jsonify(success=IPContainer.removeIPfromNetwork(str(user), str(_type), str(ip)))

@app.route("/getNetworkSize/<user>/<_type>", methods=['GET'])
@token_requiered
def getNetworkSize(current_user, user, _type):
    return jsonify(user=user, network=_type, size=IPContainer.getNetworkSize(str(user), str(_type)))

@app.route("/getData/<user>/<_type>", methods=['GET'])
@token_requiered
def getData(current_user, user, _type):
    return jsonify(user=user, network=_type, data=IPContainer.getData(str(user), str(_type)))

@app.route("/status/<user>", methods=['GET'])
@token_requiered
def statusUser(current_user, user):
    return IPContainer.getAllData(str(user))

@app.route("/dropUsers", methods=['DELETE'])
@token_requiered
def _dropUsers(current_user):
    IPContainer._dropUsers()
    return jsonify(success=True)

@app.route("/dropData", methods=['DELETE'])
@token_requiered
def _dropData(current_user):
    IPContainer._dropData()
    return jsonify(success=True)

#############################
#   Token authentication    #
#############################
@app.route("/APIUser", methods=['POST'])
@token_requiered
def addAPIUser(current_user):
    data = request.get_json()
    done = IPContainer.addAPIUser(data['username'], data['password'])
    return jsonify(success=done)
    
@app.route("/APIUser", methods=['GET'])
@token_requiered
def getAllAPIUsers(current_user):
    return IPContainer.getAllAPIUsers()

@app.route("/APIUser/<public_id>", methods=['GET'])
@token_requiered
def getAPIUser(current_user, public_id):
    return IPContainer.getAPIUser(public_id)

@app.route("/APIUser/<public_id>", methods=['DELETE'])
@token_requiered
def deleteAPIUser(current_user, public_id):
    return IPContainer.deleteAPIUser(public_id)

@app.route("/login", methods=['GET'])
def login():
    auth = request.authorization
    
    if not auth or not auth.username or not auth.password:
        return make_response('Could not verify.', 401, {'WWW-Authenticate':'Basic realm="Login required."'})

    return IPContainer.login(auth.username, auth.password)

if __name__ == "__main__":
    app.run()