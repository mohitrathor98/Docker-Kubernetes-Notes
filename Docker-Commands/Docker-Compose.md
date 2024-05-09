`docker compose up` : Builds images and containers and starts them

    By default, docker compose up command starts the container in attached mode. If we provide `-d` flag to it then it starts in detached mode.

`docker compose down`: Stops all the compose services, i.e., containers and removes them as well.

    Down command deletes containers and networks but doesn't deletes volumes by default.
    To delete volumes with compose down command we need to provide `-v` flag to it.


`docker compose up --build`: This flag ensures that images are built every time compose is getting up. Otherwise, compose will use if any pre-existing image.

`docker compose build`: Only builds images and not start containers.