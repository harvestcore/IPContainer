# -*- coding: utf-8 -*-
import unittest, json, requests, time
from requests import *
from requests.auth import HTTPBasicAuth

url = 'https://ipcontainer-docker.herokuapp.com'
username = 'test'
password = 'test'

# url = 'http://localhost:5000'
# username = 'test'
# password = 'test'

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

    def test_c_login(self):
        response = requests.get(url + '/login', auth=HTTPBasicAuth(username, password))
        self.assertEqual(response.status_code, 200, "Devuelve codigo correcto.")
        self.assertIsInstance(response.json()['token'], str, "Devuelve string como token.")
        
    def test_d_devuelve_401_si_no_hay_token(self):
        response = requests.get(url + '/NOUsers')
        self.assertEqual(response.status_code, 401, "Devuelve codigo correcto (401)")
        
    def test_e_devuelve_lista_usuarios_api(self):
        response = requests.get(url + '/APIUser', headers={'x-access-token':token})
        self.assertEqual(response.status_code, 200, "Devuelve codigo correcto")
        self.assertIsInstance(response.json()['apiusers'], list, "Devuelve lista de usuarios.")
        self.assertIsInstance(response.json()['noofusers'], int, "Devuelve entero como numero de usuarios.")

    def test_g_vaciar_tablas(self):
        response = requests.delete(url + '/dropUsers', headers={'x-access-token':token})
        self.assertEqual(response.status_code, 200, "Devuelve codigo correcto")
        self.assertEqual(response.json()['success'], True, "Vacia usuarios")

        response = requests.delete(url + '/dropData', headers={'x-access-token':token})
        self.assertEqual(response.status_code, 200, "Devuelve codigo correcto")
        self.assertEqual(response.json()['success'], True, "Vacia datos")

    def test_h_agrega_usuarios(self):        
        response = requests.post(url + '/User/user1', headers={'x-access-token':token})
        self.assertEqual(response.status_code, 200, "Devuelve codigo correcto")
        self.assertEqual(response.json()['success'], True, "Usuario 1 agregado")
        
        response = requests.post(url + '/User/user2', headers={'x-access-token':token})
        self.assertEqual(response.status_code, 200, "Devuelve codigo correcto")
        self.assertEqual(response.json()['success'], True, "Usuario 2 agregado")
        
        response = requests.get(url + '/existsUser/user1', headers={'x-access-token':token})
        self.assertEqual(response.status_code, 200, "Devuelve codigo correcto")
        self.assertEqual(response.json()['exists'], True, "Existe el usuario 1")
        
        response = requests.get(url + '/existsUser/user2', headers={'x-access-token':token})
        self.assertEqual(response.status_code, 200, "Devuelve codigo correcto")
        self.assertEqual(response.json()['exists'], True, "Existe el usuario 2")
        
        response = requests.get(url + '/NOUsers', headers={'x-access-token':token})
        self.assertEqual(response.status_code, 200, "Devuelve codigo correcto")
        self.assertEqual(response.json()['users'], 2, "Numero de usuarios correcto")
        
    def test_i_elimina_usuario(self):
        response = requests.delete(url + '/User/user2', headers={'x-access-token':token})
        self.assertEqual(response.status_code, 200, "Devuelve codigo correcto")
        self.assertEqual(response.json()['success'], True, "Usuario 2 eliminado")
        
    def test_j_elimina_usuario_no_existente(self):
        response = requests.delete(url + '/User/user99', headers={'x-access-token':token})
        self.assertEqual(response.status_code, 200, "Devuelve codigo correcto")
        self.assertEqual(response.json()['success'], False, "Usuario 99 no eliminado")
        
    def test_k_crea_red(self):
        response = requests.post(url + '/Network/user1/dns', headers={'x-access-token':token})
        self.assertEqual(response.status_code, 200, "Devuelve codigo correcto")
        self.assertEqual(response.json()['success'], True, "Crea red correctamente.")
        
        response = requests.get(url + '/existsNetwork/user1/dns', headers={'x-access-token':token})
        self.assertEqual(response.status_code, 200, "Devuelve codigo correcto")
        self.assertEqual(response.json()['exists'], True, "La red existe")
        
    def test_l_agrega_ip_a_red_existente(self):
        ip = {'data':{'dns1':'5.5.5.5', 'dns2':'5.5.5.5', 'nombre':'test'}}
        ip2 = {'data':{'dns1':'10.10.10.10', 'dns2':'10.10.10.10', 'nombre':'test2'}}

        response = requests.post(url + '/IPNetwork/user1/dns', headers={'x-access-token':token, 'content-type':'application/json'}, json=ip)
        self.assertEqual(response.status_code, 200, "Devuelve codigo correcto")
        self.assertEqual(response.json()['success'], True, "IP 1 agregada a la red existente.")
        
        response = requests.post(url + '/IPNetwork/user1/dns', headers={'x-access-token':token, 'content-type':'application/json'}, json=ip2)
        self.assertEqual(response.status_code, 200, "Devuelve codigo correcto")
        self.assertEqual(response.json()['success'], True, "IP 2 agregada a la red existente.")
        
        response = requests.get(url + '/SzNetwork/user1/dns', headers={'x-access-token':token})
        self.assertEqual(response.status_code, 200, "Devuelve codigo correcto")
        self.assertEqual(response.json()['size'], 2, "Red con tamaño 2")
        
    def test_m_elimina_ip_de_red_existente(self):
        ip = {'ip':'5.5.5.5'}
        response = requests.delete(url + '/IPNetwork/user1/dns', headers={'x-access-token':token, 'content-type':'application/json'}, json=ip)
        self.assertEqual(response.status_code, 200, "Devuelve codigo correcto")
        self.assertEqual(response.json()['success'], True, "IP 1 agregada a la red existente.")
        
        response = requests.get(url + '/SzNetwork/user1/dns', headers={'x-access-token':token})
        self.assertEqual(response.status_code, 200, "Devuelve codigo correcto")
        self.assertEqual(response.json()['size'], 1, "Red con tamaño 1")
        
    def test_v_comprobar_heroku(self):
        url = 'https://ipcontainer.herokuapp.com'
        username = 'test'
        password = 'test'

        login = requests.get(url + '/login', auth=HTTPBasicAuth(username, password))
        token = login.json()['token']
        self.assertIsInstance(token, str, "Devuelve string como token.")

        response = requests.get(url)
        self.assertEqual(response.status_code, 200, "Devuelve codigo correcto.")
        self.assertEqual(response.json()['status'], 'OK', "Devuelve estado correcto.")

        response = requests.get(url + '/status')
        self.assertEqual(response.status_code, 200, "Devuelve codigo correcto.")
        self.assertEqual(response.json()['status'], 'OK', "Devuelve estado correcto.")

    def test_w_comprobar_produccion(self):
        url = 'http://35.234.128.65'
        username = 'test'
        password = 'test'

        login = requests.get(url + '/login', auth=HTTPBasicAuth(username, password))
        token = login.json()['token']
        self.assertIsInstance(token, str, "Devuelve string como token.")

        response = requests.get(url)
        self.assertEqual(response.status_code, 200, "Devuelve codigo correcto.")
        self.assertEqual(response.json()['status'], 'OK', "Devuelve estado correcto.")

        response = requests.get(url + '/status')
        self.assertEqual(response.status_code, 200, "Devuelve codigo correcto.")
        self.assertEqual(response.json()['status'], 'OK', "Devuelve estado correcto.")       

    def test_z_finaliza_vaciando_tablas(self):
        response = requests.delete(url + '/dropUsers', headers={'x-access-token':token})
        self.assertEqual(response.status_code, 200, "Devuelve codigo correcto")
        self.assertEqual(response.json()['success'], True, "Vacia usuarios")
        
        response = requests.delete(url + '/dropData', headers={'x-access-token':token})
        self.assertEqual(response.status_code, 200, "Devuelve codigo correcto")
        self.assertEqual(response.json()['success'], True, "Vacia datos")

if __name__ == '__main__':
	unittest.main()
