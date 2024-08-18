### Node js project

1. Auth API : to generate tokens for authenticating users

2. Users API : to create and login users. (No DB or files -- dummy data).

3. Task API: Return a list of stored tasks and store new tasks.

- Users API communicate with Auth API to verify tokens

- Auth API and Users API will be part of same pod and communicate internally.

- Tasks API will be another pod.

