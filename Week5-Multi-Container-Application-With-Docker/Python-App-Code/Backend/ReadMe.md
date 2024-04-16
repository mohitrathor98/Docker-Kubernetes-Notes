## Backend for Goals APP

-- A flask app 

    Takes request to set, view and delete goals

`/sample` to see json data for set or delete goal

`docker build -t "goal-backend:1.0" .`

Running container with mount volume: `docker run -p 5000:5000 --name flask-app-goals -v "$(pwd):/app" goal-backend:1.0`

To run the container as part of network: `docker run --network mongo-net -p 5000:5000 --name flask-app-goals -v "$(pwd):/app" goal-backend:1.0`