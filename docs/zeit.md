# Despliegue en Zeit

[Link](https://proyecto-nferyfmstq.now.sh/)

El despliegue en Zeit es bastante sencillo. Lo primero es registrarnos en [Zeit](https://zeit.co/) e instalar su cliente:

```bash
npm install -g now
```

Una vez instalado nos dirijimos al directorio local donde tenemos el proyecto y creamos el archivo *now.json*. Este archivo es el que indica la versión que queremos usar de Zeit (en este caso v1, pues queremos que construya el contenedor).

```json
{
    "features": {
        "cloud": "v1"
    },
    "version": 1
}
```

Tras esto ejecuto lo siguiente:

```bash
sudo now -A ./now.json --public
```

- *-A ./now.json*: Indica donde se encuentra el archivo *now.json*.
- *--public*: Indica que queremos hacer un despliegue público.

Al ejecutar comenzará a construirse el contenedor y nos dará la url donde se encuentra desplegada nuestra app.