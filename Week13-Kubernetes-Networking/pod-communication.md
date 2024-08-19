### Communication between pods and containers.

#### Communication between containers of same pod

- Add environment variable for the container address.
- Place the env variable at the places where we need to communicate.

- For communication between containers in the same pod `localhost` can be used.