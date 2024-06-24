#### Multi-Build Container

    We can use multiple images and commands in single docker file based on our needs.


##### Dockerfile sample

``` 
    // First we will deploy node image and
    // Prepare files for React APP
    FROM node:14-alpine as build
    WORKDIR /app
    COPY package.json .
    RUN npm install
    COPY . .
    RUN npm run build

    // Now we will copy those file
    // in the nginx server and access the application
    // using it.
    FROM nginx:stable-alpine
    COPY --from=build /app/build /usr/share/nginx/html
    EXPOSE 80
    CMD ["nginx", "-g", "daemon off;"]
```