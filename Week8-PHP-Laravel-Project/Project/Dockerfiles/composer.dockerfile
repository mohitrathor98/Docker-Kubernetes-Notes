FROM composer:latest

WORKDIR /var/www/html

# ignore-platform-reqs ensures when we run we avoid
# any warning or errors that some dependencies 
# are missing
ENTRYPOINT [ "composer", "--ignore-platform-reqs" ]