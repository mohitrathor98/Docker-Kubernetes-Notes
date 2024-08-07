### Declarative Approach

- We need to write yaml files to deploy object.
- The file contains description of all the things we need.
- At last, we apply the yaml file using `kubectl apply -f file.yaml`

### How to write an object file?

Sample deployment file present: deployment.yaml

##### apiVersion

- All object files have apiVersion defined.
- We can find more details in documentation of kubernetes.
    `apiVersion: app/v1`

##### kind

- We need to specify the kind of object we want to create.
- It can be deployment, job, services, etc.
    `kind: deployment`

##### metadata

- Metadata contains name of objects, namespaces, etc.
- More information can be found in documentations.

    ```
    metadata:
        name: my-dep
    ```

##### spec

- specifications of objects that needs to be applied.
- There can be multiple specs in one configuration file.

- One for each object that needs to be created.
- For ex: if a deployment needs pod then we will have 
    1. spec for whole deployment
    2. One spec pod that needs to be deployed

Note: ***There will be only one pod per deployment***

##### replicas

- comes under spec.
- we can define number of replicas of objects needs to be created.
- can be zero.

##### selector

- must be defined in specification of the main object that needs to be created(which is defined in kind).

##### matchLabels:

- A key inside selector.
- Here, we define labels of the pod which should be controlled by deployment (in this case).
- Since, deployment takes care of pod re-intialization, scaling, etc, it needs to have control of few pod specifications.

- Deployment will control only those pods whole label matches with what mentioned here.

##### template

- We can define the description of pods for the object


#### labels

- Inside labels we can define key and value both of our choice.

#### containers:

- We can have multiple containers defined for pods.

    ```
    spec: # for deployment object
      replicas: 2
      selector:
        matchLabels:
          app: my-dep-pod
      template:
        metadata:
          labels:
            app: my-dep-pod
        spec: # for pod object
          containers:
            - name: my-dep-container-1
              image: academind/kube-first-app:1 
            - name: my-dep-container-2
              image: academind/kube-first-app:2
    ```

#### ports

- for services, we need to expose ports.
- ports takes protocol key as well which is by default `TCP`
- port key defines on what client port we can connect to
- targetPort: port on which the application inside the container is listening.

- We can have multiple ports exposed

  ```
  ports:
    - protocol: 'TCP'
      port: 80
      targetPort: 8080
    - protocol: 'TCP'
      port: 5000
      targetPort: 5000
  ```

#### type

- Type of service.
- On same indentation level as ports.

Note: ***For Services on minikube, we still need to run the minikube command: `minikube service service_name`***

***Anytime, after the deployment, we can change certain parameters like replicas in configuration file and run the same apply command for it to take affect***

***To delete the resources created by file: `kubectl delete -f=deployment.yaml,service.yaml`***

***We can have multiple configuration inside one yaml file. They just need to be separated by three dashes.`---`***

#### matchExpressions

- An alternative to matchLabels.
- This provides different ways to select the objects using labels.

- We can have operator like 'In', 'NotIn', etc.
- We can have a list of values for key.

  ```
  matchExpressions:
    - {key: app, operator: NotIn, values: [Second-pod, first-pod]}
  ```

#### livenessProbe

- Configures how kubernetes should check if container is up and running
- Without this, it just check if any error occurred in the run of container.
- However, using liveness probes, we can specify which kind of error to check and which to ignore when restarting the pods.

- Below configuration, will tell k8s to check if we are getting a success code, on http call of '/' on port 8080.

- It will check after 10 second of interval.
- And wait for 5 seconds initially, when container starts.

  ```
    livenessProbe:
      httpGet:
        path: /
        port: 8080
      periodSeconds: 10
      initialDelaySeconds: 5
  ```