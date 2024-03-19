#### Connecting with Internet

    Connecting with Internet works with docker container without any extra steps.


#### Connecting to the host machine

`host.docker.internal` <br>
We need to provide this instead of local host. Docker translates this as the IP of the host machine.


#### Connecting with other containers

##### Naive Method:
Get the IP of the other container and use it to connect with it to our container. -- Get it using `docker container inspect` command.

    But the issue here is that the IP of container is hardcoded and will needed to be changed every time the IP changes.

##### Better Method

    Docker Networks