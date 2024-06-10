### Deployment of applications which can be single container or multi-container to a production machine

##### Producion machine will be an AWS EC2 host or any other cloud service.

### A sinle containarized app deployment to production server.

    We will be creating the app on development, push it to docker hub and on production we will pull the image from hub and run container.


### Steps to deploy and run docker containers on EC2

    1. Create and launch EC2 instance, VPC(Virtual Private cloud) and security group.
    2. Configure security group to expose all required ports to WWW.
    3. Connect to instance through SSH, install docker and run container.

