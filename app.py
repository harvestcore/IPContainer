import json
from flask import Flask, jsonify
from src.ipcontainer import IPContainer

app = Flask(__name__)
ipc = IPContainer()

@app.route("/")
def hello():
    return "works :-)"

@app.route("/addUser/<user>")
def addUser(user):
    if ipc.addUser(str(user)):
        return jsonify(success=True)
    else:
        return jsonify(success=False)

@app.route("/removeUser/<user>")
def removeUser():
    if ipc.removeUser(user):
        return jsonify(success=True)
    else:
        return jsonify(success=False)

@app.route("/getNumberOfUsers", methods=['GET'])
def getNumberOfUsers():
    return jsonify(users=ipc.getNumberOfUsers())

@app.route("/getNumberOfNetworks", methods=['GET'])
def getNumberOfNetworks():
    return jsonify(networks=ipc.getNumberOfNetworks())

@app.route("/existNetwork/<user>/<_type>")
def existNetwork(user, _type):
    if ipc.existNetwork(str(user), str(_type)):
        return jsonify(exists=True)
    else:
        return jsonify(exists=False)

@app.route("/createNetwork/<user>/<_type>")
def createNetwork(user, _type):
    if ipc.createNetwork(str(user), str(_type)):
        return jsonify(success=True)
    else:
        return jsonify(success=False)

@app.route("/removeNetwork/<user>/<_type>")
def removeNetwork(user, _type):
    if ipc.removeNetwork(str(user), str(_type)):
        return jsonify(success=True)
    else:
        return jsonify(success=False)

@app.route("/addIPtoNetwork/<user>/<_type>/<ip>")
def addIPtoNetwork(user, _type, ip):
    if ipc.addIPtoNetwork(str(user), str(_type), str(ip)):
        return jsonify(success=True)
    else:
        return jsonify(success=False)
    

@app.route("/removeIPfromNetwork/<user>/<_type>/<ip>")
def removeIPfromNetwork(user, _type, ip):
    if ipc.removeIPfromNetwork(str(user), str(_type), str(ip)):
        return jsonify(success=True)
    else:
        return jsonify(success=False)

@app.route("/getNetworkSize/<user>/<_type>")
def getNetworkSize(user, _type):
    return jsonify(user=user, network=_type, size=ipc.getNetworkSize(str(user), str(_type)))

@app.route("/getData/<user>/<_type>")
def getData(user, _type):
    return jsonify(user=user, network=_type, data=ipc.getData(str(user), str(_type)))

@app.route("/_dropUsers")
def _dropUsers():
    if ipc._dropUsers():
        return jsonify(success=True)
    else:
        return jsonify(success=False)

@app.route("/_dropData")
def _dropData():
    if ipc._dropData():
        return jsonify(success=True)
    else:
        return jsonify(success=False)

if __name__ == "__main__":
    app.run()