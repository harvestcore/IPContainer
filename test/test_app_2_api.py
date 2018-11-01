# -*- coding: utf-8 -*-
import unittest, json, requests
from requests import *
from requests.auth import HTTPBasicAuth

url = 'https://ipcontainer.herokuapp.com'
username = 'test'
password = 'test'

login = requests.get(url + '/login', auth=HTTPBasicAuth(username, password))
token = login.json()['token']

class testAPI(unittest.TestCase):
    def test_a_main(self):
        response = requests.get(url)
        self.assertEqual(response.status_code, 200, "Devuelve codigo correcto.")
        self.assertEqual(response.json()['status'], 'OK', "Devuelve estado correcto.")

    def test_b_status(self):
        response = requests.get(url + '/status')
        self.assertEqual(response.status_code, 200, "Devuelve codigo correcto.")
        self.assertEqual(response.json()['status'], 'OK', "Devuelve estado correcto.")
        self.assertIsInstance(response.json()['networks'], dict, "Devuelve json de redes.")
        self.assertIsInstance(response.json()['noofnetworks'], int, "Devuelve entero como numero de redes.")
        self.assertIsInstance(response.json()['noofusers'], int, "Devuelve entero como numero de usuarios.")

    def test_c_login(self):
        response = requests.get(url + '/login', auth=HTTPBasicAuth(username, password))
        self.assertEqual(response.status_code, 200, "Devuelve codigo correcto.")
        self.assertIsInstance(response.json()['token'], str, "Devuelve string como token.")

    def test_d_devuelve_401_si_no_hay_token(self):
        response = requests.get(url + '/getNumberOfUsers')
        self.assertEqual(response.status_code, 401, "Devuelve codigo correcto (401)")

    def test_e_devuelve_lista_usuarios_api(self):
        login = requests.get(url + '/login', auth=HTTPBasicAuth(username, password))
        token = login.json()['token']
        response = requests.get(url + '/APIUser', headers={'x-access-token':token})
        self.assertEqual(response.status_code, 200, "Devuelve codigo correcto")
        self.assertIsInstance(response.json()['apiusers'], list, "Devuelve lista de usuarios.")
        self.assertIsInstance(response.json()['noofusers'], int, "Devuelve entero como numero de usuarios.")

    # def test_f_crear_usuario_api(self):
    #     login = requests.get(url + '/login', auth=HTTPBasicAuth(username, password))
    #     response = requests.post(url + '/APIUser', headers={'x-access-token':login.json()['token'], 'content-type':'application/json'}, json={'username':'testuser', 'password':'testuser'})
    #     self.assertEqual(response.status_code, 200, "Devuelve codigo correcto")
    #     self.assertEqual(response.json()['success'], True, "Crea correctamente al API User")

    def test_g_vaciar_tablas(self):
        response = requests.delete(url + '/dropUsers', headers={'x-access-token':token})
        self.assertEqual(response.status_code, 200, "Devuelve codigo correcto")
        self.assertEqual(response.json()['success'], True, "Vacia usuarios")
        response = requests.delete(url + '/dropData', headers={'x-access-token':token})
        self.assertEqual(response.status_code, 200, "Devuelve codigo correcto")
        self.assertEqual(response.json()['success'], True, "Vacia datos")

    def test_h_agrega_usuarios(self):        
        response = requests.post(url + '/addUser/user1', headers={'x-access-token':token})
        self.assertEqual(response.status_code, 200, "Devuelve codigo correcto")
        self.assertEqual(response.json()['success'], True, "Usuario 1 agregado")
        
        response = requests.post(url + '/addUser/user2', headers={'x-access-token':token})
        self.assertEqual(response.status_code, 200, "Devuelve codigo correcto")
        self.assertEqual(response.json()['success'], True, "Usuario 2 agregado")

        response = requests.get(url + '/existsUser/user1', headers={'x-access-token':token})
        self.assertEqual(response.status_code, 200, "Devuelve codigo correcto")
        self.assertEqual(response.json()['exists'], True, "Existe el usuario 1")

        response = requests.get(url + '/existsUser/user2', headers={'x-access-token':token})
        self.assertEqual(response.status_code, 200, "Devuelve codigo correcto")
        self.assertEqual(response.json()['exists'], True, "Existe el usuario 2")

        response = requests.get(url + '/getNumberOfUsers', headers={'x-access-token':token})
        self.assertEqual(response.status_code, 200, "Devuelve codigo correcto")
        self.assertEqual(response.json()['users'], 2, "Numero de usuarios correcto")

    def test_i_elimina_usuario(self):
        response = requests.delete(url + '/removeUser/user2', headers={'x-access-token':token})
        self.assertEqual(response.status_code, 200, "Devuelve codigo correcto")
        self.assertEqual(response.json()['success'], True, "Usuario 2 eliminado")

    def test_j_elimina_usuario_no_existente(self):
        response = requests.delete(url + '/removeUser/user99', headers={'x-access-token':token})
        self.assertEqual(response.status_code, 200, "Devuelve codigo correcto")
        self.assertEqual(response.json()['success'], False, "Usuario 99 no eliminado")

    def test_k_crea_red(self):
        response = requests.post(url + '/createNetwork/user1/dns', headers={'x-access-token':token})
        self.assertEqual(response.status_code, 200, "Devuelve codigo correcto")
        self.assertEqual(response.json()['success'], True, "Crea red correctamente.")

        response = requests.get(url + '/existsNetwork/user1/dns', headers={'x-access-token':token})
        self.assertEqual(response.status_code, 200, "Devuelve codigo correcto")
        self.assertEqual(response.json()['exists'], True, "La red existe")

    def test_l_crea_red_ya_existente(self):
        response = requests.post(url + '/createNetwork/user1/dns', headers={'x-access-token':token})
        self.assertEqual(response.status_code, 200, "Devuelve codigo correcto")
        self.assertEqual(response.json()['success'], False, "Red existente no creada.")

    def test_m_agrega_ip_a_red_existente(self):
        ip = {'data':{'dns1':'5.5.5.5', 'dns2':'5.5.5.5', 'nombre':'test'}}
        ip2 = {'data':{'dns1':'10.10.10.10', 'dns2':'10.10.10.10', 'nombre':'test2'}}

        response = requests.post(url + '/addIPtoNetwork/user1/dns', headers={'x-access-token':token, 'content-type':'application/json'}, json=ip)
        self.assertEqual(response.status_code, 200, "Devuelve codigo correcto")
        self.assertEqual(response.json()['success'], True, "IP 1 agregada a la red existente.")

        response = requests.post(url + '/addIPtoNetwork/user1/dns', headers={'x-access-token':token, 'content-type':'application/json'}, json=ip2)
        self.assertEqual(response.status_code, 200, "Devuelve codigo correcto")
        self.assertEqual(response.json()['success'], True, "IP 2 agregada a la red existente.")

        response = requests.get(url + '/getNetworkSize/user1/dns', headers={'x-access-token':token})
        self.assertEqual(response.status_code, 200, "Devuelve codigo correcto")
        self.assertEqual(response.json()['size'], 2, "Red con tamaño 2")


if __name__ == '__main__':
	unittest.main()
