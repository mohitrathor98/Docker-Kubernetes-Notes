### Communication between pods and containers.

#### Communication between containers of same pod

- Add environment variable for the container address.
- Place the env variable at the places where we need to communicate.

- For communication between containers in the same pod `localhost` can be used.


#### Communication between containers of different pods

- IP of pods keep on changing after restart.
- Hence, we need to create service for the pods to communicate with them.

- If pods needs to be inaccessible from outside the cluster, we can configure service type as `ClusterIP`

##### Multiple ways of accessing service IPs

1. Deploy the service whose IP we need, and provide it's IP to the env variable in the deployment file of pod that needs the IP.

2. Kubernetes creates an environment variable for all the services in. We can use that environment variable in our code.

        Pattern of the variables created are: `SERVICE_NAME_SERVICE_HOST` -- All in caps
        Ex: AUTH_SERVICE_SERVICE_HOST

3. Using Domain name (core DNS) - This DNS is known only inside the cluster.

    Domain name of a service is its's service name and namespace: `service-name.namespace`
    Ex: auth-service.default