#### REQUIREMENTS

    A mongodb container which stores data which persists even if we remove the current container and run next one.
    Additionally, We should make authentication enabled.

#### TO Make Data Persist

    MongoDB stores it data file at "/data/db". So, we can create a named volume.

#### FOR Authentication

    Modifying /etc/mongod.conf file present inside the mongo container, using a dockerfile to replace it.
    security:
        authorization: enabled
