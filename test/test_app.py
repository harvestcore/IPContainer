# -*- coding: utf-8 -*-
import unittest
import json
from src.ipcontainer import IPContainer

with open('./src/json/ip.json') as f:
        data_ip = json.load(f)

with open('./src/json/dns.json') as f2:
        data_dns = json.load(f2)

data = {"dns1": "5.5.5.5", "dns2": "5.5.5.5", "nombre":"angel"}

class testIPContainer(unittest.TestCase):
    def setUp(self):
        self.ipc = IPContainer()
        
    def test_should_initialize_object_OK(self):
        self.assertIsInstance(self.ipc, IPContainer, "Objeto creado correctamente")

    def test_vacia_tablas(self):
        self.ipc._dropUsers()
        self.assertEqual(self.ipc.getNumberOfUsers(), 0, "Tabla usuarios vaciada.")
        self.ipc._dropData()
        self.assertEqual(self.ipc.getNumberOfUsers(), 0, "Tabla datos vaciada.")

    def test_agrega_usuarios(self):
        self.ipc.addUser("test_user1")
        self.assertEqual(self.ipc.existUser("test_user1"), True, "Usuario 1 agregado correctamente.")
        self.ipc.addUser("test_user2")
        self.assertEqual(self.ipc.existUser("test_user2"), True, "Usuario 2 agregado correctamente.")

    def test_elimina_usuario(self):
        self.ipc.removeUser("test_user2")
        self.assertEqual(self.ipc.existUser("test_user2"), False, "Usuario eliminado correctamente.")

    def test_elimina_usuario_que_no_existe(self):
        self.assertEqual(self.ipc.removeUser("test_user5"), False, "No elimina usuario que no existe.")

    def test_crea_red(self):
        self.ipc.createNetwork("test_user1", "dns", data)
        self.assertEqual(self.ipc.existNetwork("test_user1", "dns") , True, "Nueva red creada correctamente")

    def test_crea_red_que_ya_existe(self):
        self.assertEqual(self.ipc.createNetwork("test_user1", "dns", data), False, "Red existente no creada")

if __name__ == '__main__':
	unittest.main()
