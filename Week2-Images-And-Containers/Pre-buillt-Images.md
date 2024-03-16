_We can get pre-build images as well. __Docker Hub__ is the place from where
we can get the images._

### How to get containers running from pre-built images?
```
docker run <image_name>
```
Docker checks if the image is available locally first, then it checks online at docker hub. If the image is available on the docker hub, docker pulls it and runs the container.

```
docker ps -a
```
Lists all the containers which ran on the system.


```
docker run -it <image_name>
```
The it flag will tell docker that the host need to have an interactive session with the container machine.

