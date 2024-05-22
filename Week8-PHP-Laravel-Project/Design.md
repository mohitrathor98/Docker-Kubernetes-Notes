1. Nginx web server application
    -- Communicates with PHP interpreter
    -- Server for the PHP web app

2. PHP Interpreter
    -- Used to interpret the source code
    -- Communicates with the nginx

3. MySql Database
    -- Database for the application
    -- Communicates with PHP interpreter as that is where code will execute

Utility containers

1. Composer
    -- A laravel or php tool
    -- Used to create environment with necessary libraries for Laravel and PHP

2. Laravel Artisan
    -- A CLI for Laravel which provides multiple commands
    -- Commands can be used to easily interact with laravel application

3. npm
    -- Few components of Laravel uses npm
    -- For ex: Laravel uses vue.js