## Python Multi-Container Application

#### TODO:

```
[X] A mongoDB container

    [X] Data should persist if we remove container
    [X] Access should be limited for users -- Authentication
```  

```
[X] Web Application that accepts and returns json Data

    [X] Takes request that allows user to set, view and delete goals
    [X] Stores the goals into a database
    [X] Also store a log file -- Backend events of GET, POST, etc.
    [X] The log file should persist
    [X] Live source code update
    [X] Before storing check if goal is duplicate

    [X] When interacting with database, application provides credentials.
```

```
[ ] Frontend -- Single Page Web Application based upon React

    [X] A React application that runs on the browser
    [X] A label, textfield and submit button
    [X] Below of the submit button list of goals, a message if empty
    [X] If we click on goals ==> It gets deleted.
    [X] Containerize the React APP
    [ ] Live updates when the source code changes.
    [ ] Communicates with the backend API to add, view and delete goals
```

ScratchPad

--> The frontend code should send the goal to backend
--> The backend code will store the goal to db

--> The frontend on reload will ask the backend for GOal list that will be given from db
--> Then frontend will list that data

--> If User clicks on goal, frontend will signal the backend to delete the goals and send the list again. 