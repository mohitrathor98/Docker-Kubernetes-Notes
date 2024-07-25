### Kubernetes Volumes

- Kubernetes supports a broad variety of volume types/ drivers.

    1. "Local" Volumes (on nodes)
    2. Cloud-provider specific volumes

- Volume lifetime depends on the pod lifetime.
- Hence, ***survives container restarts but not pod***

 