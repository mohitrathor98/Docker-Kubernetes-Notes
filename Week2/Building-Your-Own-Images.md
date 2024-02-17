#### We can build our own image over a pre-built images to run our own code base. For example, running our python application over a pre-built python interpreter image.

## Writing a Dockerfile

### Dockerfile
Used to create your own images. It is a special file recognized by docker. It contains a set of instructions for our own image.

```
FROM baseImageName
```
Docker file starts with the base image that we want to use. It can be an image that we built ourselves as well.

```
COPY . /app
```
This command is used to copy the local files into the container. The command expects two arguments here. First one is which files to copy and second is where to copy inside the container.

`.` --> This means to copy all the file present at the location of Dockerfile

`/app` --> This means to create a directory named app if not present  inside root of the container and copy the files there.

```
WORKDIR /app
```
By default working directory inside a docker container is root. WORKDIR command can be used to change the working directory of the container.

```
RUN npm install
```
This command can be used to run a command inside the container at the working directory location.

```
CMD ["node", "server.js"]
```
This is used to run command once a container is started based on the image.

<em><strong>The difference of CMD from RUN is that RUN gets executed when image is built, while CMD gets executed when a container is started.</em></strong>

```
EXPOSE 80
```
Since docker containers are isolated, we cannot access it's port unless we expose a port.

#### Note:

    EXPOSE 80 in the Dockerfile in the end is optional. It documents that a process in the container will expose this port. But you still need to then actually expose the port with -p when running docker run. So technically, -p is the only required part when it comes to listening on a port. Still, it is a best practice to also add EXPOSE in the Dockerfile to document this behavior.