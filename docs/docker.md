# Despliegue en Docker

[**Repositorio en DockerHub**](https://hub.docker.com/r/harvestcore/ipcontainer)



Contenido del Dockerfile:

```dockerfile
FROM python:3.6

COPY . ./ipc

RUN pip install --upgrade pip
RUN cd ./ipc && pip3 install -r requirements.txt

ENV SECRET_KEY=
ENV MYSQL_KEY=

EXPOSE 5000

ENTRYPOINT cd ./ipc && python3 application.py
```



Para crear la imagen:

```bash
docker image build -t harvestcore/ipcontainer .
```



Login en Docker y push de la imagen:

```bash
docker login
docker push harvestcore/ipcontainer
```

