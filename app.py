import json
from flask import Flask, jsonify
from src.ipcontainer import IPContainer

app = Flask(__name__)

@app.route("/", methods=['GET'])
def index():
    return jsonify(status="OK")

@app.route("/status", methods=['GET'])
def status():
    return jsonify(users=IPContainer.getNumberOfUsers(), networks=IPContainer.getNumberOfNetworks())

@app.route("/addUser/<user>", methods=['POST'])
def addUser(user):
    return jsonify(success=IPContainer.addUser(str(user)))

@app.route("/removeUser/<user>", methods=['POST'])
def removeUser(user):
    return jsonify(success=IPContainer.removeUser(str(user)))

@app.route("/getNumberOfUsers", methods=['GET'])
def getNumberOfUsers():
    return jsonify(users=IPContainer.getNumberOfUsers())

@app.route("/existsUser/<user>", methods=['GET'])
def existUser(user, _type):
    return jsonify(exists=IPContainer.existUser(str(user)))

@app.route("/getNumberOfNetworks", methods=['GET'])
def getNumberOfNetworks():
    return jsonify(networks=IPContainer.getNumberOfNetworks())

@app.route("/existsNetwork/<user>/<_type>", methods=['GET'])
def existNetwork(user, _type):
    return jsonify(exists=IPContainer.existNetwork(str(user), str(_type)))

@app.route("/createNetwork/<user>/<_type>", methods=['POST'])
def createNetwork(user, _type):
    return jsonify(success=IPContainer.createNetwork(str(user), str(_type)))

@app.route("/removeNetwork/<user>/<_type>", methods=['POST'])
def removeNetwork(user, _type):
    return jsonify(success=IPContainer.removeNetwork(str(user), str(_type)))

@app.route("/addIPtoNetwork/<user>/<_type>/<ip>", methods=['POST'])
def addIPtoNetwork(user, _type, ip):
    return jsonify(success=IPContainer.addIPtoNetwork(str(user), str(_type), str(ip)))
    
@app.route("/removeIPfromNetwork/<user>/<_type>/<ip>", methods=['POST'])
def removeIPfromNetwork(user, _type, ip):
    return jsonify(success=IPContainer.removeIPfromNetwork(str(user), str(_type), str(ip)))

@app.route("/getNetworkSize/<user>/<_type>", methods=['GET'])
def getNetworkSize(user, _type):
    return jsonify(user=user, network=_type, size=IPContainer.getNetworkSize(str(user), str(_type)))

@app.route("/getData/<user>/<_type>", methods=['GET'])
def getData(user, _type):
    return jsonify(user=user, network=_type, data=IPContainer.getData(str(user), str(_type)))

@app.route("/_dropUsers", methods=['GET'])
def _dropUsers():
    IPContainer._dropUsers()

@app.route("/_dropData", methods=['GET'])
def _dropData():
    IPContainer._dropData()

if __name__ == "__main__":
    app.run(debug=True, use_reloader=True)