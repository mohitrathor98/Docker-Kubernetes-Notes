When running a docker mode, we may want to have an interactive session with the
docker shell.

### How to do it?
<hr>

#### Using docker run -- When creating a container

`-i` : This flag creates an interactive session(STDIN open) even if container is not attached.

`-t` : Allocates a Pseudo-TTY -- Creates a terminal

If we combine both then, it means a terminal exposed to the container with STDIN channel open.

```
docker run -it <image>
```


#### Using docker start -- When starting an exited container

<i>If we start a container in attached mode, without using `-i` flag, we won't be able to create a STDIN channel.</i>

```
docker start -a -i <container_name>
```

###### Doubt? what happens if we do not use -a?

```
docker start -i <container_name> 
--> works same as the above command
```