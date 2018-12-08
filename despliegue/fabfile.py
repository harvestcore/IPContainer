from fabric.api import *

env.use_ssh_config = True

def test():
    env.hosts = ['ubuntu']

def database_up():
    sudo('chown ubuntu:ubuntu /var/run/docker.sock')
    run('docker run -d --name ipcsql harvestcore/ipcontainer-mysql')
    run('sleep 20')

def app_up():
    run('echo $MYSQL_KEY')
    run('echo $SECRET_KEY')
    run('docker run -p 80:5000 -e "MYSQL_KEY=$MYSQL_KEY" -e "SECRET_KEY=$SECRET_KEY" --name ipc harvestcore/ipcontainer')

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
    dockerprune()
    database_up()
    app_up()

def ipcontainer_down():
    database_down()
    app_down()

def deploy():
    run('whoami')