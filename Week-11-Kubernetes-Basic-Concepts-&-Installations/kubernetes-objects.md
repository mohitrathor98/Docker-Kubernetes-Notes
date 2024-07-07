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