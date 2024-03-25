## Python Multi-Container Application

#### TODO:

```
[X] A mongoDB container

    [X] Data should persist if we remove container
    [X] Access should be limited for users -- Authentication
```  

```
[ ] Web Application that accepts and returns json Data

    [ ] Takes request that allows user to set, view and delete goals
    [ ] Stores the goals into a database
    [ ] Also store a log file -- Backend events of GET, POST, etc.
    [ ] The log file should persist
    [ ] Live source code update
```

```
[ ] Frontend -- Single Page Web Application based upon React

    [X] A React application that runs on the browser
    [X] A label, textfield and submit button
    [ ] Below of the submit button list of goals, a message if empty
    [ ] Communicates with the backend API to add, view and delete goals
    [ ] If we click on goals ==> It gets deleted.
    [ ] Live updates when the source code changes.
```