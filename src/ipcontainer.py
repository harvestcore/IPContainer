from .databases_json import Users, Data
import json, simplejson

def mergeJSON(jsonA, jsonB):
    
    for i in range(len(jsonB["data"])):
        jsonA["data"].append(jsonB["data"][i])

    return jsonA
    

class IPContainer():

    def existUser(self, _username):
        ret = False
        if Users.exist(_username):
            ret = True

        return ret

    def addUser(self, _username):
        ret = False
        if not Users.exist(_username):
            Users.insert(_username)
            ret = True

        return ret

    def removeUser(self, _username):
        ret = False
        if Users.exist(_username):
            Users.delete(_username)
            ret = True

        return ret

    def getNumberOfUsers(self):
        return Users.tableSize()

    def getNumberOfNetworks(self):
        return Data.tableSize()

    def existNetwork(self, _username, _type):
        ret = False
        if Data.exist(_username, _type):
            ret = True

        return ret

    def createNetwork(self, _username, _type):
        ret = False
        if Users.exist(_username):
            if not Data.exist(_username, _type):
                Data.createNetwork(_username, _type)
                ret = True

        return ret

    def removeNetwork(self, _username, _type):
        ret = False
        if Users.exist(_username):
            if Data.exist(_username, _type):
                Data.delete(_username, _type)
                ret = True

        return ret

    def addIPtoNetwork(self, _username, _type, _data):
        ret = False
        if Users.exist(_username):
            if Data.exist(_username, _type):
                datalist = Data.getData(_username, _type)
                Data.updateData(_username, _type, datalist.append(_data))
                ret = True

        return ret

    def removeIPfromNetwork(self, _username, _type, _ip):
        ret = False
        if Users.exist(_username):
            if Data.exist(_username, _type):
                data = Data.getData(_username, _type)

                if _type == "dns":
                    for i in range(len(data["data"]) - 1):
                        print(len(data["data"]))
                        if data["data"][i]["dns1"] == _ip or data["data"][i]["dns2"] == _ip:
                            data["data"].pop(i)
                            ret = True

                else:
                    for i in range(len(data["data"]) - 1):
                        if data["data"][i]["ip"] == _ip:
                            data["data"].pop(i)
                            ret = True

                if ret:
                    Data.updateData(_username, _type, data)

        return ret

    def getNetworkSize(self, _username, _type):
        if Users.exist(_username):
            if Data.exist(_username, _type):
                return len(Data.getData(_username, _type)["data"])

    def getData(self, _username, _type):
        if Users.exist(_username):
            if Data.exist(_username, _type):
                return Data.getData(_username, _type)

    def _dropUsers(self):
        Users._dropTable()

    def _dropData(self):
        Data._dropTable()
