# API

## General

| Método |      URI       |     Parámetros     |                            Return                            |              Función               |
| :----: | :------------: | :----------------: | :----------------------------------------------------------: | :--------------------------------: |
|  GET   |       /        |         -          |                       {"status":"OK"}                        |                OK.                 |
|  GET   |    /status     |         -          |    {"users":"`int`", "noofnetworks":`int` "networks":{}}     | Estado general y resumen de redes. |
|  GET   | /status/`user` | Nombre de usuario. | {"username": `user`,
    "noofnetworks": `int`,
    "networks": []} |    Resumen de redes de `user`.     |



## Usuarios

| Método |        URI         |     Parámetros     |        Return         |             Función             |
| :----: | :----------------: | :----------------: | :-------------------: | :-----------------------------: |
|  POST  |  /addUser/`user`   | Nombre de usuario. | {"success":`boolean`} |       Agrega un usuario.        |
|  POST  | /removeUser/`user` | Nombre de usuario. | {"success":`boolean`} |       Elimina un usuario.       |
|  GET   | /getNumberOfUsers  |         -          |    {"users":`int`}    | Consulta el número de usuarios. |
|  GET   | /existsUser/`user` | Nombre de usuario. | {"exists":`boolean`}  | Comprueba si existe un usuario. |
|  GET   |    /_dropUsers     |         -          | {"success":`boolean`} |   Elimina todos los usuarios.   |



## Redes

| Método |                   URI                   |                   Parámetros                   |        Return         |                           Función                            |
| :----: | :-------------------------------------: | :--------------------------------------------: | :-------------------: | :----------------------------------------------------------: |
|  POST  |      /createNetwork/`user`/`type`       |        Nombre de usuario. Tipo de red.         | {"success":`boolean`} |        Crea una nueva red para `user` de tipo `type`.        |
|  POST  |      /removeNetwork/`user`/`type`       |        Nombre de usuario. Tipo de red.         | {"success":`boolean`} |           Elimina la red de `user` de tipo `type`.           |
|  POST  |   /addIPtoNetwork/`user`/`type`/`ip`    | Nombre de usuario. Tipo de red. IP a agregar.  | {"success":`boolean`} |     Agrega a la red de tipo `type` de `user` la IP `ip`.     |
|  POST  | /removeIPfromNetwork/`user`/`type`/`ip` | Nombre de usuario. Tipo de red. IP a eliminar. | {"success":`boolean`} |    Elimina de la red de tipo `type` de `user` la IP `ip`.    |
|  GET   |          /getNumberOfNetworks           |                       -                        | {"networks":"`int`"}  |                 Consulta el número de redes.                 |
|  GET   |      /existsNetwork/`user`/`type`       |        Nombre de usuario. Tipo de red.         | {"exists":`boolean`}  |                 Comprueba si existe una red.                 |
|  GET   |      /getNetworkSize/`user`/`type`      |        Nombre de usuario. Tipo de red.         |   {"size":"`int`"}    |    Devuelve el tamaño de la red de tipo `type` de `user`.    |
|  GET   |         /getData/`user`/`type`          |        Nombre de usuario. Tipo de red.         |      {"data":[]}      | Devuelve todas las IP asociadas a la red de tipo `type` de `user`. |
|  GET   |               /_dropData                |                       -                        | {"success":`boolean`} |                   Elimina todas las redes.                   |



## Formatos JSON

### IP

```json
{
    "ip": "",
    "mac": "",
    "gateway": "",
    "network": "",
    "netmask": "",
    "broadcast": "",
    "tipo": "",
    "nombre": "",
    "dispositivo": ""
}
```



### Red IP

```json
{
    "user":"",
    "data": [] 
}
```



### DNS

```json
{
    "dns1": "",
    "dns2": "",
    "nombre": ""
}
```



### Red DNS

```json
{
    "user":"",
    "data": [] 
}
```



