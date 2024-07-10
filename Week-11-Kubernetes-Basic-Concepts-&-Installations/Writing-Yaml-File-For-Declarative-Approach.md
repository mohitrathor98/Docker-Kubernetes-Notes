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


#### template

- We can define the description of pods for the object


#### labels

- Inside labels we can define key and value both of our choice.

#### containers:

- We can have multiple containers defined for pods.

    ```
    spec: # for deployment object
      replicas: 2
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