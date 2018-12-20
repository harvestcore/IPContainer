# Despliegue final

## IAAS
Como IAAS utilizo Google Cloud por varias razones. La primera es porque es mucho más fácil de utilizar (a mi parecer) que Microsoft Azure; tanto el cliente como la interfaz web me ha resultado más fácil de usar en el caso de GC. La segunda es la facturación; en GC la puedes consultar muy fácil (en Azure no la encuentras ni queriendo). Y por último, por cosas que pasan en la vida me pulí el saldo de Azure y me han bloqueado la cuenta, pero esto me ha servido para conocer y usar Google Cloud.

## Sistema Operativo
He elegido Ubuntu 16.04 LTS, un sistema con mantenimiento a largo plazo con el que he trabajado bastante anteriormente y en el que IPContainer funciona a las mil maravillas.

## Docker
Para ejecutar el microservicio utilizo [Docker](docker.md), pues es una manera sencilla de desplegarlo, además de que de este modo se encuentra más aislado y seguro.

## Base de datos
La base de datos que utiliza el microservicio está alojada también en Google Cloud. La latencia es bastante baja y no es relativamente costosa. Utilizo tres bases de datos: una para el microservicio alojado en GC, otra para tests y la última para los despliegues del microservicio en Heroku. [Más info.](bd.md)

## Otra documentación
- [**Despliegue con Fabric**](despliegue.md)
- [**Provisionamiento con Ansible**](provision.md)
- [**Orquestamiento con Vagrant**](vagrant.md)