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