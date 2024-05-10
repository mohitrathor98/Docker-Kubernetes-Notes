Utility commands or container basically means using the pre-built images to run our code without installing the complete environment in our system.

Ex: By developing a node application on pre-built node container the set, we can about the setup process of node on our system.

#### TO get a node environment

    dokcer run -it node

#### Executing a command inside a running container

    docker exec <container> "command"
    ==> docker exec -it node "npm init"

#### Provide a command when starting a container

    docker run -it node "npm init"
    ==> This will overwirte the default command of the container mentioned in the image.

#### ENTRYPOINT

    Instead of CMD in dockerfile if we provide ENTRYPOINT then we can append to the command mentioned for this while running the container.

    Ex: 
    ENTRYPOINT ["python3"]

    docker run -it python-app app.py
    ==> This will run the app.py script when starting the container.

#### Using the ENTRYPOINT in compose

    docker compose run python-app app.py
    ==> Here, python-app is the name of service mentioned in the compose file

`docker compose run` is used for running a specific service mentioned in the compose file.