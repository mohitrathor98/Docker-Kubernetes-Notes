#### Attached Mode: We are listening to the docker in the terminal shell.

#### Detached Mode: We have closed the connection to the container in the shell but container is still running and can be connected on listening port.

```
docker run
```
This command by default triggers a container in attached mode.


```
docker start
```
Used to start an exited container. Start it in detached mode.


```
docker start <container_name>
```
Re-starts the exited container. Container starts in the background -- `Detached Mode`.

```
docker start -a <container_name>
```
Re-starts the exited container in `attached mode`.


```
docker run -p 8000:80 -d <image_id>
```
Now docker run will start a container in detached mode.


```
docker attach <container_name>
```
Re-attach to the attached command.

```
docker logs <container_name>
```
To see all the past logging by the docker container.

`-f` : To follow on `docker logs` command

