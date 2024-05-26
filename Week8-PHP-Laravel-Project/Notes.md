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

# View the app at

    <IP>:8000

# To Run things in smooth way 
    docker composer up -d --build

#### Note: When the container is up for first time, Laravel application needs db migration to run. Once it is run, Laravel gets up and running in the browser.
##### How to run migration?

    In the browser, refresh 2-3 times, it will ask to run migration

    Or, run the laravel artisian commands to migrate.


#### Note: putting entrypoint in composer file, overrides the entrypoint in the dockerfile or image being used. Or appends to it if already not present
    