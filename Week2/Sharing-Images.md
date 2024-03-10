#### We can share images using two methods

<ol><li><b>Docker File</b></li>
We can provide the complete set of code, dependencies and docker file.
This docker file can be used to build an image.
<li><b>Share the image itself</b></li>
We can share images via <ul> <li>Docker Hub</li>
<li> Private Repositories </li></ul>
</ol>

```
Docker Hub is an official registry for docker containers but there are others.
Several Private registry also handles these in and out of images.
```

To push or pull the images from and to the docker hub we use
```
 docker push < image-name >
 docker pull < image-name >
```

To do the same for a private registry
We need to provide a host name `hostname:image-name`


To push our image to docker hub we need to give it the same image name as the repo name we created on docker hub. Also need to provide the username.
Ex: `mohirath/hello-world`

To rename or retag a docker image we can use docker tag command
`docker tag oldname:tag newname:tag`

`docker login` command to connect with the docker hub account
