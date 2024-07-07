### Deployment of pods

    -- We will deploy pod using deployment object of kubernetes
    
1. Builing the image

    - Build image using docker file
        `docker build . -t kube-action-start`

2. Check if cluster is running

    - `minikube status`

There two ways to create kubernetes objects:
    1. Imperative Approach
    2. Declarative Approach

1. Imperative Approach

    `kubectl create deployment <deployment-name> --image=<image_name>`

    Note: Here image_name should be present on docker hub and not locally.
          Kubernetes doesn't check on local machine.

2. Declarative Approach: TBD

-- To get deployment: `kubectl get deployment`
-- To delete deployment: `kubectl delete deployment`