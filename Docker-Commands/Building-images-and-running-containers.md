## Building images and running containers

```
docker build .
```
This is used to build an image from a dockerfile.

`.` --> Path of docker file. Here, it means that the path from where we are running this command has the dockerfile.

After the image is built, we get an image id.
```
docker run <image-id>
````
This starts a container based upon the image-id provided.

```
docker stop <container-name>
```
This stops the running container.

```
docker run -p 3000:80 <image-id>
```
Here, we are exposing a port of container and accessing on a system port.

`-p` --> For publishing a port

`3000:80` --> System port where we are using the container services is 3000 and 80 is the port where docker container is listening.


```
docker start <container_name>
```
Re-starts the exited container. Container starts in the background -- Detached Mode.

```
docker run -p 8000:80 -d <image_id>
```
Now docker run will start a container in detached mode.

```
docker run -it <image_name>
```
The it flag will tell docker that the host need to have an interactive session with the container machine.
