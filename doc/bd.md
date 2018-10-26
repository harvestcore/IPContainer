# Resumen de base de datos de IPContainer

## BD Producción

La base de datos está compuesta por tres tablas, las cuales tienen la siguiente estructura:

### Usuarios

|  Nombre  |   Tipo    | Tamaño |              Otros              |
| :------: | :-------: | :----: | :-----------------------------: |
|    id    |   `int`   |   7    | Clave primaria. Auto increment. |
| username | `varchar` |   35   |        Único. Not null.         |



### Datos redes

|  Nombre  |   Tipo    | Tamaño |              Otros              |
| :------: | :-------: | :----: | :-----------------------------: |
|    id    |   `int`   |   7    | Clave primaria. Auto increment. |
| username | `varchar` |   35   |            Not null.            |
|   type   | `varchar` |   4    |            Not null.            |
|   data   |  `json`   |   -    |                -                |



### Usuarios API

|  Nombre   |   Tipo    | Tamaño |              Otros              |
| :-------: | :-------: | :----: | :-----------------------------: |
|    id     |   `int`   |   7    | Clave primaria. Auto increment. |
| public_id | `varchar` |   50   |            Not null.            |
|   name    | `varchar` |   35   |            Not null.            |
| password  | `varchar` |  100   |            Not null.            |



## BD Test

Para realizar los tests (ya obsoletos) de forma local he utilizado la siguiente *"base de datos"*:

- *Usuarios*: Lista de strings.

- *Data*: Lista de json, los cuales tienen la siguiente estructura:

  ```json
  {
      "username":"",
      "type":"",
      "data": []
  }
  ```








