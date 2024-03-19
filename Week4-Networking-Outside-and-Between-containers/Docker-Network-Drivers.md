## Docker Network Drivers

Docker Networks actually support different kinds of "Drivers" which influence the behavior of the Network.

The default driver is the 
#### `Bridge driver` - Containers can find each other by name if they are in the same Network.

The driver can be set when a Network is created, simply by adding the `--driver option`.

`docker network create --driver bridge my-net`

    Of course, if you want to use the "bridge" driver, you can simply omit the entire option since "bridge" is the default anyways.

#### Docker also supports these alternative drivers:

`host`: 
    
    For standalone containers, isolation between container and host system is removed (i.e. they share localhost as a network)

`overlay`:

     Multiple Docker daemons (i.e. Docker running on different machines) are able to connect with each other. Only works in "Swarm" mode which is a dated / almost deprecated way of connecting multiple containers

`macvlan`: 

    You can set a custom MAC address to a container - this address can then be used for communication with that container

`none`: 

    All networking is disabled.

`Third-party plugins`: 

    You can install third-party plugins which then may add all kinds of behaviors and functionalities.