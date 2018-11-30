FROM mysql:8

ENV MYSQL_DATABASE ipcdb
ENV MYSQL_ROOT_PASSWORD root

COPY ./ipcdb.sql /docker-entrypoint-initdb.d
COPY . ipc

RUN apt-get update
RUN apt-get install -y python3-dev python3-pip
# RUN pip3 install --upgrade pip
RUN pip3 install -r ipc/requirements.txt

EXPOSE 5000

# CMD [ "python3", "application.py" ]