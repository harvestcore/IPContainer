# IPContainer

[![License: GPL v3](https://img.shields.io/badge/License-GPL%20v3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0) [![Build Status](https://travis-ci.com/harvestcore/IPContainer.svg?branch=master)](https://travis-ci.com/harvestcore/IPContainer) [![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://ipcontainer.herokuapp.com/) [![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://ipcontainer-docker.herokuapp.com/)

---

### Links
- [Despliegue Heroku](https://ipcontainer.herokuapp.com/)
- [Despliegue Contenedor](https://ipcontainer-docker.herokuapp.com)
- [Contenedor](https://hub.docker.com/r/harvestcore/ipcontainer)

Despliegue final: 35.246.104.37


### Otros links
- `Inactivo` [Despliegue Zeit](https://proyecto-ohyqiqsrxe.now.sh/)
- `Inactivo` [Despliegue Azure](https://ipcontainer.azurewebsites.net/)

---

## ¿Qué es?

IPContainer es un microservicio centrado en el almacenamiento y gestión básica de direcciones IP. Permite tener almacenadas una serie de direcciones IP en un mismo lugar, agrupadas por tipo de red:

- **PAN** (Personal Area Network)
- **LAN** (Local Area Network)
- **WAN** (Wide Area Network)
- **SAN** (Storage Area Network)
- **VLAN** (Virtual Local Area Network)
- **WLAN** (Wireles Local Area Network)

Por otro lado permite almacenar direcciones IP de servidores **DNS**.

---

## ¿Por qué?

La idea surge tras necesitar un lugar donde tener una serie de direcciones IP organizadas y almacenadas en un mismo lugar, sin depender de mirar archivos de configuración o uso de otras aplicaciones.

Más info:

- [**Documentación**](#doc)
- [**Web del proyecto**](https://harvestcore.github.io/es/ipcontainer/index.html)
- [**Web del repositorio**](https://harvestcore.github.io/IPContainer)

---

## Herramientas y servicios

- [**Python**](https://www.python.org/): Lenguaje principal de programación.
  - [**Flask**](http://flask.pocoo.org/): Framework principal.
  - [**SQLAlchemy**](https://www.sqlalchemy.org/): Como [**ORM**](https://es.wikipedia.org/wiki/Mapeo_objeto-relacional).
- [**MariaDB**](https://mariadb.org/): Gestor de base de datos.
- [**Travis-CI**](https://travis-ci.org/): Para integración contínua.
- [**Heroku**](https://www.heroku.com/): Como PaaS.
- [**Microsoft Azure**](https://azure.microsoft.com/es-es/): Como IaaS.
- [**Google Cloud**](https://cloud.google.com/): Como IaaS.

---
<div id='doc' />

## Documentación:

- [**Instalación**](docs/install.md)
- [**API**](docs/api.md)
- [**Autenticación con token**](docs/auth.md)
- [**Base de datos**](docs/bd.md)
- [**CI Test**](docs/tests.md)
- [**Despliegue final en Google Cloud**](docs/desplieguefinal.md)
- [**Provisionamiento con Ansible**](docs/provision.md)
- [**Configuración de Vagrant con Google Cloud**](docs/vagrant.md)
- [**Despliegue con Fabric**](docs/despliegue.md)
- [**Docker (Docker Hub y Heroku)**](docs/docker.md)
- [**Despliegue en Heroku**](docs/heroku.md)
- [**Despliegue en Microsoft Azure**](docs/azure.md)
- [**Despliegue en Zeit**](docs/zeit.md)
- [**Archivo de configuración de TravisCI**](.travis.yml)
- `Inactivo` [**ReadTheDocs**](https://ipcontainer.readthedocs.io)

---

## Pasos a seguir en el desarrollo de IPContainer

- [x] Descripción general.
- [x] Elección de herramientas para su desarrollo.
- [x] Integración continua. Tests.
- [x] Autenticación con token.
- [x] Despliegue del microservicio en un PaaS.
- [x] Despliegue en docker.
- [x] Despliegue automático a las plataformas de producción.
