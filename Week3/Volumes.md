### Volumes 
    -- A built-in feature of docker.
    -- Filesystem on the host machine which are mounted/mapped to the container.
    -- It persists even if container gets deleted.


#### Anonymous Volumes

    To create an anonymous volume, we need to mention it in the dockerfile

```
    VOLUME [ " directory which should de made persist”]
    Ex:
    VOLUME [“/app/db”]
```

    -- Location of the storage on host machine gets decided by the docker.
    -- These volumes gets deleted once the container is deleted.


#### Named Volumes

    -- They are persisted even after container deletion.
    -- We cannot access it directly on the host machine.

To create a named volume, while starting the container we provide arguments to the command.

`-v volume-name:path-inside-container`
