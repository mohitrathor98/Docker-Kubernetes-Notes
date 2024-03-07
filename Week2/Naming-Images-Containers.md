
### Naming Images

Name for the images have two parts
<ol>
<li>Name: It can be the base name of the image</li>
<li>Tags: It can be a version number or name</li>
</ol>

`-t`: flag can be used with `docker build` command to give an image its name and tag.
```
docker build -t demo:latest .
```

<em>To remove tagged images: `docker images prune -a`</em>


### Naming containers

`--name` : providing name to the container when starting container using `docker run`

```
docker run -it --name lol <image_name>
```