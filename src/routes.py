def routes():
    main = {'ruta':'/', 'salida':'Status de la API.', 'metodo':'GET'}
    status = {'ruta':'/status', 'salida':'Status completo de la API y rutas.', 'metodo':'GET'}
    
    login = {'ruta':'/login', 'salida':'token', 'BasicAuth':{'username':'test', 'password':'test'}, 'metodo':'GET'}
    addAPIUser = {'ruta':'/APIUser', 'salida':'message', 'headers':[{'name':'x-access-token', 'value':'token'}], 'content':[{'type':'application/json', 'content':{'username':'user', 'password':'pass'}}], 'metodo':'POST'}
    getAPIUsers = {'ruta':'/APIUser', 'salida':'message', 'headers':[{'name':'x-access-token', 'value':'token'}], 'metodo':'GET'}
    getAPIUser = {'ruta':'/APIUser/<public_id>', 'salida':'API User info', 'headers':[{'name':'x-access-token', 'value':'token'}], 'metodo':'GET'}
    delAPIUser = {'ruta':'/APIUser/<public_id>', 'salida':'message', 'headers':[{'name':'x-access-token', 'value':'token'}], 'metodo':'DELETE'}

    addUser = {'ruta':'/addUser/<user>', 'salida':'success', 'headers':[{'name':'x-access-token', 'value':'token'}], 'metodo':'POST'}
    removeUser = {'ruta':'/User/<user>', 'salida':'success', 'headers':[{'name':'x-access-token', 'value':'token'}], 'metodo':'DELETE'}
    getNumberOfUsers = {'ruta':'/NOUsers', 'salida':'Number of users.', 'headers':[{'name':'x-access-token', 'value':'token'}], 'metodo':'GET'}
    existsUser = {'ruta':'/existsUser/<user>', 'salida':'exists', 'headers':[{'name':'x-access-token', 'value':'token'}], 'metodo':'GET'}
    
    getNumberOfNetworks = {'ruta':'/NONetworks', 'salida':'Number of networks.', 'headers':[{'name':'x-access-token', 'value':'token'}], 'metodo':'GET'}
    existsNetwork = {'ruta':'/existsNetwork/<user>/<type>', 'salida':'exists', 'headers':[{'name':'x-access-token', 'value':'token'}], 'metodo':'GET'}
    createNetwork = {'ruta':'/Network/<user>/<type>', 'salida':'success', 'headers':[{'name':'x-access-token', 'value':'token'}], 'metodo':'POST'}
    removeNetwork = {'ruta':'/Network/<user>/<type>', 'salida':'success', 'headers':[{'name':'x-access-token', 'value':'token'}], 'metodo':'DELETE'}
    addIPtoNetwork = {'ruta':'/IPNetwork/<user>/<type>', 'salida':'success', 'headers':[{'name':'x-access-token', 'value':'token'}], 'content':[{'type':'application/json', 'data':{'ip':{'ip': '','mac': '','gateway': '','network': '','netmask': '','broadcast': '','tipo': '','nombre': '','dispositivo': ''}}}, {'type':'application/json', 'data':{'dns':{'dns1': '','dns2': '','nombre': ''}}}], 'metodo':'POST'}
    removeIPfromNetwork = {'ruta':'/IPNetwork/<user>/<type>', 'salida':'success', 'headers':[{'name':'x-access-token', 'value':'token'}], 'content':[{'type':'application/json', 'data':{'ip':''}}], 'metodo':'DELETE'}
    getNetworkSize = {'ruta':'/SzNetwork/<user>/<type>', 'salida':'Tamaño de la red.', 'headers':[{'name':'x-access-token', 'value':'token'}], 'metodo':'GET'}
    getData = {'ruta':'/Data/<user>/<type>', 'salida':'Datos de la red.', 'headers':[{'name':'x-access-token', 'value':'token'}], 'metodo':'GET'}
    statusUser = {'ruta':'/status/<user>', 'salida':'Datos de las redes del usuario.', 'headers':[{'name':'x-access-token', 'value':'token'}], 'metodo':'GET'}
    
    return {'main':main, 'status': status, 'login':login, 'addAPIUser':addAPIUser, 'getAPIUsers':getAPIUsers, 'getAPIUser':getAPIUser, 'delAPIUser':delAPIUser, 'addUser':addUser, 'removeUser':removeUser, 'getNumberOfUsers':getNumberOfUsers, 'existsUser':existsUser, 'getNumberOfNetworks':getNumberOfNetworks, 'existsNetwork':existsNetwork, 'createNetwork':createNetwork, 'removeNetwork':removeNetwork, 'addIPtoNetwork':addIPtoNetwork, 'removeIPfromNetwork':removeIPfromNetwork, 'getNetworkSize':getNetworkSize, 'getData':getData, 'statusUser':statusUser}
