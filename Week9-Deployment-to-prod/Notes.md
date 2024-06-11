### Deployment of applications which can be single container or multi-container to a production machine

##### Producion machine will be an AWS EC2 host or any other cloud service.

### A sinle containarized app deployment to production server.

    We will be creating the app on development, push it to docker hub and on production we will pull the image from hub and run container.


### Steps to deploy and run docker containers on EC2

    1. Create and launch EC2 instance, VPC(Virtual Private cloud) and security group.
    2. Configure security group to expose all required ports to WWW.
    3. Connect to instance through SSH, install docker and run container.


#### 1. Create and Launch EC2 instance

    -- Create an AWS account
    -- Free tier EC2 instance needs to be launched
    -- Type : Amazon linux
    -- Create key-pair for the instance (.pem)

#### 3. Connecting to instance through SSH, installing docker and run container

    -- .pem file genrated should have 600 permission
    -- ssh -i "first-instance.pem" ec2-user@ec2-3-25-114-88.ap-southeast-2.compute.amazonaws.com

    Installing docker

    `sudo yum install docker`
    `sudo systemctl start docker`

    -- Pushing our image to docker hub
    
    `docker build . -t mohitrathor/node-app-basic`
    `docker push mohitrathor/node-app-basic`

    -- Running the image in EC2

    `docker run -d --rm -p 80:80 mohitrathor/node-app-basic`

    -- To Access the web server running on EC2

     ==> Access public IP address mentioned in the Amazon web console

#### 2. Configuring security group to expose all required ports

    We need to configure security groups for EC2 instance so that we can communicate with that instance.
    There are two kinds of rules:
    
    1. Outbound rules: This allows from which outside resources the EC2 instance can communicate.

    2. Inbound rules: This is what we should configure if we want to communicate with EC2 from outside

    We need to configure an inbound rule for https/http on port 80 for our application to work.

    http://<public IP of ec2 instance>