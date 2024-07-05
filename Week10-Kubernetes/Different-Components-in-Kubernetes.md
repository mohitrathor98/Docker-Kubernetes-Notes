### Components in Kubernetes.

1. Pods: 
    - Smallest possible unit in Kubernetes.
    - A pod contains one or more containers.
    - Pod = Containers + Their required resources(like volumes).

2. Node:
    - A machine or virtual machine instance where pods run.
    - Two kind of nodes:
        a. Worker Node
        b. Master Node

3. Proxy: 
    - Defined on nodes to decide network communication of pod(s).
    - Decides how container inside pod can communicate with themselves or from outside world.

4. Control Plane:
    - Control centre on master node
    - Manages multiple worker nodes, workload distribution and scaling.

5. Cluster:
    - Master node + Worker Node configuration 
    - A set of node which are running the contanrized application or control nodes.

6. Worker Node:
    - Activities managed by the master node.
    - Can have multiple pods running on it.
    - Pods can have one or more container and volumes doing their work.

    - Pods gets scheduled by master node.

7. Kubelet:
    - Runs on the worker nodes which helps in communicating between nodes and pods.

8. Kube-proxy:
    - A network which provides communication between pods, containers and nodes.

9. API Server:
    - Runs on master node
    - Kubelet running on compute node communicates with it.

10. Scheduler:
    - Watches for new pods.
    - Selects worker node to run pods upon.
    - Communicates with API Server which in turn communicates with kubelet running on worker.

11. Kube-Controller-Manager
    - Watches and controls worker nodes
    - Corrects number of pods, etc.

12. Cloud-Controller-Manager
    - Like Kube-Controller BUT for a specific cloud provider.
    - Knows how to interact with cloud provider resources.  

13. Services:
    - A logical set of pods with a unique, pod- and container- independent IP address.