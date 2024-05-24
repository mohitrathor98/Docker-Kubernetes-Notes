#### What if we don't provide ENTRYPOINT or CMD in our dockerfile?

    In this case ENTRYPOINT or CMD mentioned in the base image of the dockerfile is used.
    
    If we mention it then, the ENTRYPOINT or CMD gets appended(in case of base image doesn't have it) and overwritten(in case it already have one defined).

##### Running composer to build Laravel project/template

`docker compose run --rm composer create-project --prefer-dist laravel/laravel .`


##### Configure Database information in .env file of Laravel project

    Provide Database name, User, Password and also in host provide container name of the database.


# starting multiple services at once

`docker compose run --rm --build -d server php nginx`

    Alternatively we can provide 'depends_on' in one service and it will trigger with other being started.