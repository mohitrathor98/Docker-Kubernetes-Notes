### Kubernetes Volumes

- Kubernetes supports a broad variety of volume types/ drivers.

    1. "Local" Volumes (on nodes)
    2. Cloud-provider specific volumes

- Volume lifetime depends on the pod lifetime.
- Hence, ***survives container restarts but not pod***

- https://kubernetes.io/docs/concepts/storage/volumes/

- There are different types of volumes that kubernetes supports and offers.

    1. csi
    2. emptyDir
    3. hostPath
- These types determines how the data is stored in the volumes outside of container.
- They don't influence how volumes works inside of container.

### Creating volumes in kubernetes

- Volumes are the part of pod.
- So, we need to define volume where, we are defining the pod inside yaml file.

#### emptyDir volume

- emptyDir creates a new empty directory whenever the pod starts.
- The data persists as long as pod is alive.
- Below lines means we want default configuration of this volume type
    `emptyDir: {}`

- Downside: If there are multiple replicas, and if one of them crashes, then the volume gets inaccessible for a moment.

#### hostPath volume

- Helps to create volume on host machine.
- This way multiple pod can access same volume.
    ```
        hostPath:
          # path on the host machine
          path: /data
          type: DirectoryOrCreate
          # type means it will check for this directory on host machine and creates if it doesn't exists.
    ```

- ***This can also be used to have some pre-existing data at the volume path.***

- Downside: Dependent on host, so if multiple compute nodes are there then creates same issue as emptyDir.

#### CSI volume

- Container Storage Interface
- Allows any type of file storage system to connect with the container.
    Ex: AWS EFS CSI Driver
