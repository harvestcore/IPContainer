# Instalación de IPContainer

## Instalar dependencias
```bash
pip3 install -r requirements.txt
```

## Variables de entorno
### Conexión a la BD (MySQL)
```bash
export MYSQL_KEY="mysql+mysqlconnector://<user>:<pass>@<host>:<port>/<bd>"
```

### Secret key (Token Auth)
En mi caso es una cadena de 64 caracteres.
```bash
export SECRET_KEY="<secret_key>"
```

## Ejecutar
Por defecto se ejecuta en el puerto 5000.
```bash
python3 application.py
```