## Docker-Compose

Automating Multi-Container setups

### Why do we even need it?

    Using docker compose, we can add multiple docker build and run commands in once configuration file and run that file using a set of orchestration commands.

##### Note: Docker compose is not suitable for running multiple containers on multiple hosts. They are suited for multiple containers on a single host.

### Writing docker compose file

    We can define services, which are containers.
    Each containers can have defined their ports, volumes, env variables, networks, etc.
