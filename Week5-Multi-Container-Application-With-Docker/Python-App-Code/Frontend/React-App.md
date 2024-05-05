#### Creating a new react app

    npx create-react-app <project-name>

    ==> This creates react project with node_modules, src files, etc.

#### Starting the development server

    npm start

    ==> From the react project directory


### Modify App.js to add new components to the app

### How to install the react dependencies for already created project?

    Go to the react project directory and run (provided package.json is present)

    npm install

#### Commands
`docker build -t "react-goal-ap:1.0" .`

`docker run -d -p 3000:3000 -v "$(pwd)/src:/app/src" --name "goal-frontent" react-goal-ap:1.0`