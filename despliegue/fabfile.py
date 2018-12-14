from fabric.api import *

env.use_ssh_config = True

def staging():
    env.hosts = ['ubuntu']

def production():
    env.hosts = ['ipcontainer']

def app_up():
    run('docker run -d -p 80:5000 --env-file ~/env.list --name ipc harvestcore/ipcontainer')

def app_down():
    run('docker stop ipc')

def dockerprune():
    run('docker system prune -f')

def dockerimages():
    run('docker images')

def dockerps():
    run('docker ps')

def update_app():
    run('docker pull harvestcore/ipcontainer')

def ipc_up():
    execute(dockerprune)
    execute(app_up)

def ipc_down():
    execute(app_down)