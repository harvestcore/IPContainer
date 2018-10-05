# -*- coding: utf-8 -*-
import unittest

from src.ipcontainer import IPContainer

class testIPContainer(unittest.TestCase):
	def setUp(self):
		self.ipc = IPContainer()

	def test_should_initialize_object_OK(self):
		self.assertIsInstance(self.ipc, IPContainer, "Objeto creado correctamente")

if __name__ == '__main__':
	unittest.main()