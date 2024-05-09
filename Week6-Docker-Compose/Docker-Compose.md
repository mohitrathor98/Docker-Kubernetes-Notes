## Docker-Compose

Automating Multi-Container setups

### Why do we even need it?

    Using docker compose, we can add multiple docker build and run commands in once configuration file and run that file using a set of orchestration commands.

##### Note: Docker compose is not suitable for running multiple containers on multiple hosts. They are suited for multiple containers on a single host.

### Writing docker compose file

    We can define services, which are containers.
    Each containers can have defined their ports, volumes, env variables, networks, etc.

#### Notes on docker-compose basics

    When we close a compose service, all containers gets deleted by default. So need for --rm

<hr>

    All services defined inside a compose file share a same network. So we don't need to specify them explicitely. But if there are containers required to access different networks then we can specify them using `--networks`

<hr>

    Services name in the compose file can be used to communicate between containers in the same compose network.


### Commands

`docker compose up` : Builds images and containers and starts them

    By default, docker compose up command starts the container in attached mode. If we provide `-d` flag to it then it starts in detached mode.

`docker compose down`: Stops all the compose services, i.e., containers and removes them as well.

    Down command deletes containers and networks but doesn't deletes volumes by default.
    To delete volumes with compose down command we need to provide `-v` flag to it.



