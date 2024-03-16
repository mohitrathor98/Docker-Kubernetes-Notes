### Environment Variables

Available inside the docker file and can be accessed from the code.

```
    In dockerfile, if we mention
        ENV PORT 80
    It creates an environment variable which can be accessed by the scripts inside the container and images.
```

```
    --env PORT=8080
    If we provide this argument to docker run command then the container will run with the env variable PORT value as 8080 instead of 80 which is declared inside the dockerfile.
```

We can also create `.env` file which can contain all the environment variables.
And we can mention this file information when running the container using the docker run command.

```
    --env-file ./.env
    This means at the Working directory .env file is present containing the environment variable information.
```