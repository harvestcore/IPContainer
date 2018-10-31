# API

## General

| Método |      URI       |     Parámetros     |                          Return                          |              Función               |
| :----: | :------------: | :----------------: | :------------------------------------------------------: | :--------------------------------: |
|  GET   |       /        |         -          |                   {"status":`status`}                    |   Devuelve el status de la API.    |
|  GET   |    /status     |         -          |  {"users":"`int`", "noofnetworks":`int` "networks":{}}   | Estado general y resumen de redes. |
|  GET   | /status/`user` | Nombre de usuario. | {"username":`user`, "noofnetworks":`int`, "networks":[]} |    Resumen de redes de `user`.     |


## Usuarios

| Método |        URI         |     Parámetros     |        Return         |             Función             |
| :----: | :----------------: | :----------------: | :-------------------: | :-----------------------------: |
|  POST  |  /addUser/`user`   | Nombre de usuario. | {"success":`boolean`} |       Agrega un usuario.        |
|  DELETE  | /removeUser/`user` | Nombre de usuario. | {"success":`boolean`} |       Elimina un usuario.       |
|  GET   | /getNumberOfUsers  |         -          |    {"users":`int`}    | Consulta el número de usuarios. |
|  GET   | /existsUser/`user` | Nombre de usuario. | {"exists":`boolean`}  | Comprueba si existe un usuario. |
|  DELETE   |    /dropUsers     |         -          | - |   Elimina todos los usuarios.   |



## Redes

| Método |                   URI                   |                   Parámetros                   |        Return         |                           Función                            |
| :----: | :-------------------------------------: | :--------------------------------------------: | :-------------------: | :----------------------------------------------------------: |
|  POST  |      /createNetwork/`user`/`type`       |        Nombre de usuario. Tipo de red.         | {"success":`boolean`} |        Crea una nueva red para `user` de tipo `type`.        |
|  DELETE  |      /removeNetwork/`user`/`type`       |        Nombre de usuario. Tipo de red.         | {"success":`boolean`} |           Elimina la red de `user` de tipo `type`.           |
|  POST  |   /addIPtoNetwork/`user`/`type`/`ip`    | Nombre de usuario. Tipo de red. IP a agregar.  | {"success":`boolean`} |     Agrega a la red de tipo `type` de `user` la IP `ip`.     |
|  DELETE  | /removeIPfromNetwork/`user`/`type`/`ip` | Nombre de usuario. Tipo de red. IP a eliminar. | {"success":`boolean`} |    Elimina de la red de tipo `type` de `user` la IP `ip`.    |
|  GET   |          /getNumberOfNetworks           |                       -                        | {"networks":"`int`"}  |                 Consulta el número de redes.                 |
|  GET   |      /existsNetwork/`user`/`type`       |        Nombre de usuario. Tipo de red.         | {"exists":`boolean`}  |                 Comprueba si existe una red.                 |
|  GET   |      /getNetworkSize/`user`/`type`      |        Nombre de usuario. Tipo de red.         |   {"size":"`int`"}    |    Devuelve el tamaño de la red de tipo `type` de `user`.    |
|  GET   |         /getData/`user`/`type`          |        Nombre de usuario. Tipo de red.         |      {"data":[]}      | Devuelve todas las IP asociadas a la red de tipo `type` de `user`. |
|  DELETE   |               /dropData                |                       -                        | - |                   Elimina todas las redes.                   |



## Autenticación con token

| Método |         URI          |                   Parámetros                   |                            Return                            |                         Función                         |          Header          | Autenticación (Básica) |
| :----: | :------------------: | :--------------------------------------------: | :----------------------------------------------------------: | :-----------------------------------------------------: | :----------------------: | :--------------------: |
|  POST  |       /APIUser       |                       -                        |                    {"success":`boolean`}                     |               Agrega un usuario a la API.               | "x-access-token":`token` |           -            |
|  GET   |       /APIUser       |                       -                        |                       {"apiusers":[]}                        |          Muestra todos los usuarios de la API.          | "x-access-token":`token` |           -            |
|  GET   | /APIUser/`public_id` | `public_id` del usuario a obtener información. | {"user":{"password":`string`, "public_id":`string`, "username":`string`}} | Muestra la información asociada a un usuario de la API. | "x-access-token":`token` |           -            |
| DELETE | /APIUser/`public_id` |      `public_id` del usuario a eliminar.       |                 {"message":"User deleted."}                  |              Elimina un usuario de la API.              | "x-access-token":`token` |           -            |
|  GET   |        /login        |                       -                        |                      {"token":`string`}                      |               Logea al usuario en la api.               |            -             |     `user`:`pass`      |



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



