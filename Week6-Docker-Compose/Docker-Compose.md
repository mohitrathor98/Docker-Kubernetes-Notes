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
