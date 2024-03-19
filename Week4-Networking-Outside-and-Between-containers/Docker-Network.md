## Docker Networks

    If we create a docker network and add the containers to it, then the networking between containers gets taken care by the docker.

    We don't need to provide the IP of other containers inside the source code.

    If we just providing the name of container in place of IP, docker resolves it and helps us in communicating with the containers.

#### Step-1 is to create a network. -- Without creating we can't use it when running containers, like we use for volumes.

`docker network create <network-name>`

#### Now, when running the container, we provide `--network <network-name>` in the command and docker adds the container to the network.

`docker run --network <network-name> --name <container-name> <image-name>`

##### Instead of IP of the other containers, we provide the `name` of it in the locations we are trying to communicate with other containers.


