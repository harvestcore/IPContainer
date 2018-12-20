# Tests

Los tests de integración contínua para la clase y las URIs los he creado con el framework [Unittest](https://docs.python.org/3/library/unittest.html) y comprueban todas las funcionalidades del microservicio.

- [Test clase](../test/test_app_1_class.py)
- [Test URIs](../test/test_app_2_api.py)

Estos tests son ejecutados en [TravisCI](https://travis-ci.com/harvestcore/IPContainer) cada vez que se actualiza el repositorio del proyecto.

Todos los tests se pasa en una base de datos usada solo para este cometido. En los tests de la clase se comprueban todas las funcionalidades del microservicio, y en los tests de las URIs se comprueban también todas las funcionalidades, pero en este caso en el despliegue de IPContainer en Heroku (docker), además de que los otros despliegues funcionan.