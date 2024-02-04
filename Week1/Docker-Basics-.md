What is docker?

    -- Docker is a container tech: A tool for creating and managing containers.

What is a container?

    -- A standardized unit of software
    -- A packaging of code and its dependencies to run that code.
    
    Ex: A Node.js code requires NodeJs runtime, so code and NodeJs dependencies are packaged into a single container.
        -- Now this container can be executed anywhere and it will give same result.
    
Advantage of container:

    -- Development and Production server can have same execution environment.
    -- Multiple projects using different versions of same software can be handled.


**Docker Instalation**

<a href="https://docs.docker.com/engine/install/">Docker Installation Page</a>

Installation on Linux - Ubuntu 22.04

    1. Follow steps here https://docs.docker.com/engine/install/ubuntu/
    2. Enable root access using these steps: https://docs.docker.com/engine/install/linux-postinstall/

**Docker Tools**

    1. Docker Engine: Hosts linux VM required to run docker containers.
    2. Docker Desktop: Includes Daemon and CLI - Also installs Docker Engine
    3. Docker Hub: Service that allows to host our images in cloud.
    4. Docker Compose: Makes managing complex containers or multi-containers easier.

**Kubernetes**

    Tool to manage complex containerized applications.

