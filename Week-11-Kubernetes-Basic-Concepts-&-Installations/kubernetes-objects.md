## Kubernetes objects.

- Kubernetes works with objects.
- We can create these objects using commands and manipulate them.
- Some examples are: pods, services, volumes, deploymens, etc.

#### Pods

- Contains one or more container and/or volumes.
- Have cluster internal IP using which other pods can communicate to it.
- Multiple containers can communicate with each other using localhost.
- They are ephemeral just like container, which means data doesn’t persist when they are removed or deleted.
- We can deploy them simply as pods, or part of ‘deployment’, which is a better alternative, since, kubernetes manages pods as part of deployment and takes care of it’s creation, deletion and re-init in case of error in containers of pods.

#### Deployments

- We can deploy one or more pods using a deployment.
- We can provide number of instances of each pod, and kubernetes will manage the load of nodes while deploying the pods.
- Deployments can be paused, deleted and rolled back when needed.
- We can deploy multiple deployments containing different number of pods.

#### Services

- Exposes pods to cluster or externally
- By default, pods have internal ip private within the cluster.
- And they keep on changing
- Groups pod with shared Ip.

- kubectl expose: This command can be used to expose a pod or deployment to external world using services.
- We need to provide port that needs to be exposed and also type of service needs to be created.
    `kubectl expose deployment <dep-name> --type=LoadBalancer --port=8080`

`kubectl get services` : Can be used to list all the serivces running on node.
    - For minikube, we do not see external IP as it is just a simulation of cluster.
    - For actual cluster, we will see external IP of the services, so that we can access.

    - For minikube, we need to run one additional command to get URL for accessing
        `minikube service <dep-name>`

Note: ***Check out different types of services***