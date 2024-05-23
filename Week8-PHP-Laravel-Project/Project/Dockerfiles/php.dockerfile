FROM PHP:8.2-fpm-alpine

# Standard working directory for web based containers
WORKDIR /var/www/html

# Installing PHP dependencies
RUN docker-php-ext-install pdo pdo_mysql

