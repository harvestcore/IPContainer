# Resumen de base de datos de IPContainer

## Estructura de las tablas

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
| admin  | `tinyint` |  1   |            -            |


### Otros
Las bases de datos (tres) se encuentran alojadas en Google Cloud.
- BD para tests.
- BD para despliegues en Heroku.
- BD para despliegue en Google Cloud.
