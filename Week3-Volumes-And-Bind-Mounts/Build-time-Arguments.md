### Build Time Arguments

Variables which get set during image building.

Inside the dockerfile, we mention the variable name like: `ARG DEFAULT_PORT=8080`
To use it over other instruction like environment variable: `ENV PORT $DEFAULT_PORT`

```
We can build image and it will get build with an environment variable PORT with value 8080
```

Now, Suppose we need another image with different port value, we can do so by manipulating the build time arguments during the image creation

```
docker build -t image_name:different_port --build_arg DEFAULT_PORT=5000 .
```
