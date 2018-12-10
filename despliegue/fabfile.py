from fabric.api import *

env.use_ssh_config = True

def staging():
    env.hosts = ['ubuntu']

def production():
    env.hosts = ['ipcontainer']

def database_up():
    sudo('chown ubuntu:ubuntu /var/run/docker.sock')
    run('docker run -d -p 3306:3306 --name ipcsql harvestcore/ipcontainer-mysql')
    run('sleep 30')

def app_up():
    run('docker run -d -p 80:5000 -e MYSQL_KEY="mysql+mysqlconnector://root:root@172.17.0.2:3306/ipcdb" -e "SECRET_KEY=rQsgiA2EupfZTo7WIBY61CmHMWrUTvRBl6JiITvp1GW2uyP5rhHWEh3KZAb3R2F7" --name ipc harvestcore/ipcontainer')

def database_down():
    run('docker stop ipcsql')

def app_down():
    run('docker stop ipc')

def dockerprune():
    run('docker system prune -f')

def dockerimages():
    run('docker images')

def dockerps():
    run('docker ps')

def update_db():
    run('docker pull harvestcore/ipcontainer-mysql')

def update_app():
    run('docker pull harvestcore/ipcontainer')

def ipcontainer_up():
    execute(dockerprune)
    execute(database_up)
    execute(app_up)

def ipcontainer_down():
    execute(database_down)
    execute(app_down)