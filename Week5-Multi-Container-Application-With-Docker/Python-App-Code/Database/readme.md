#### REQUIREMENTS

    A mongodb container which stores data which persists even if we remove the current container and run next one.
    Additionally, We should make authentication enabled.

#### TO Make Data Persist

    MongoDB stores it data file at "/data/db". So, we can create a named volume.

`docker run -d -v mongodb_data:/data/db --name mongodb mongo`

To restart the same container again: `docker start mongodb`

To run the container as part of a network: `docker run -d --network mongo-net -v mongodb_data:/data/db --name mongodb mongo`

Authentication:

    -e MONGO_INITDB_ROOT_USERNAME=mongoadmin \
    -e MONGO_INITDB_ROOT_PASSWORD=secret

`docker run -d --network mongo-net -v mongodb_data:/data/db -e MONGO_INITDB_ROOT_USERNAME=mongoadmin -e MONGO_INITDB_ROOT_PASSWORD=secret --name mongodb mongo`

To interact: `mongodb://mongoadmin:secret@{container_name}:27017/`