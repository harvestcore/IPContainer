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
    return ipc.addUser(user)

@app.route("/removeUser/<user>")
def removeUser():
    return ipc.removeUser(user)

@app.route("/getNumberOfUsers")
def getNumberOfUsers():
    return ipc.getNumberOfUsers()

@app.route("/getNumberOfNetworks")
def getNumberOfNetworks():
    return ipc.getNumberOfNetworks()

@app.route("/existNetwork/<user>/<_type>")
def existNetwork(user, _type):
    return ipc.existNetwork(user, _type)

@app.route("/createNetwork/<user>/<_type>")
def createNetwork(user, _type):
    return ipc.createNetwork(user, _type)

@app.route("/removeNetwork/<user>/<_type>")
def removeNetwork(user, _type):
    return ipc.removeNetwork(user, _type)

@app.route("/addIPtoNetwork/<user>/<_type>/<ip>")
def addIPtoNetwork(user, _type, ip):
    return ipc.addIPtoNetwork(user, _type, ip)

@app.route("/removeIPfromNetwork/<user>/<_type>/<ip>")
def removeIPfromNetwork(user, _type, ip):
    return ipc.removeIPfromNetwork(user, _type, ip)

@app.route("/getNetworkSize/<user>/<_type>")
def getNetworkSize(user, _type):
    return ipc.getNetworkSize(user, _type)

@app.route("/getData/<user>/<_type>")
def getData(user, _type):
    return ipc.getData(user, _type)

@app.route("/_dropUsers")
def _dropUsers():
    return ipc._dropUsers()

@app.route("/_dropData")
def _dropData():
    return ipc._dropData()

if __name__ == "__main__":
    app.run()