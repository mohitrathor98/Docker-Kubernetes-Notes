```
docker images
--> To see the list of images on the host.
```

```
docker ps
-->Lists all the running container on the host.
```

```
docker ps -a
--> Lists all the containers which ran on the system.
```

```
docker stop <container_name1> <container_name2>...
--> To stop the containers
```

```
docker rmi <image_id>
--> To remove docker images. Only when no containers are present for that image.
```

```
docker image prune
--> Removes all the images. Only when no containers are present for that image.
```

```
docker rm <container_name1> <container_name2>...
--> To delete a stopped container
```

`--rm` : if we provide this flag to `docker run` command, the container will get deleted once it is stopped.


