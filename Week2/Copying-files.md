#### To copy the files inside and outside of container we use `docker cp` command

```
docker cp demo/. container_name:/home/test
--> Copy from demo directory of host to /home/test directory of the container
```

```
docker cp container_name:/home/test demo/.
--> Copy files out of the container.
```