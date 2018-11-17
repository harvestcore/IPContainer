# Instalación de IPContainer

## Instalar dependencias

```bash
pip3 install -r requirements.txt
```





## Variables de entorno

### Conexión a la BD

```bash
# MySQL
export MYSQL_KEY="mysql+mysqlconnector://<user>:<pass>@<host>:<port>/<bd>"

# SQLite3
export MYSQL_KEY="sqlite:///<database>.db"
```



### Secret key (Token Auth)

En mi caso es una cadena de 64 caracteres.
```bash
export SECRET_KEY="<secret_key>"
```



### Puerto

```bash
export PORT=<port>
```





## Ejecutar

En caso de no especificar la variable de entorno para el puerto Flask se ejecutará en el 5000.
```bash
python3 application.py
```





## Instalación con Docker

### Descargar la imagen de [Docker Hub](https://hub.docker.com/r/harvestcore/ipcontainer/):

```bash
docker pull harvestcore/ipcontainer
```



### Iniciar el contenedor:

#### Con puerto por defecto:

```bash
docker run harvestcore/ipcontainer
```

#### Con puerto específico:

```bash
docker run -e PORT=<port> harvestcore/ipcontainer
```

