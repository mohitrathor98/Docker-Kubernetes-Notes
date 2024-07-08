### Updating deployment

Suppose, we changed some code in our already deployed application. Now, we will need to update the image which the deployed pod is running.

1. Build image using docker build command
2. Push the image to docker hub
3. Run kubectl set image command

    `kubectl set image deployment/<dep-name> <deployed-container-name>=<image-name-to-update>:tag`

Note: ***New image will only be updated by k8s if the tag is different.***

- To check the status of updated deployment: `kubectl rollout status deployment/<dep-name>`

Note: ***Kubernetes doesn't removes old pods before new pod deployments are up and running. This helps in preventing any collaterals with the changes to shutdown the application***

### Undo the latest deployment

- Suppose, our latest deployment failed for some reason.
- New pods are crashing and we need to roll back to the previous deployment. 
    `kubectl rollout undo deployment/<dep-name>`

### Roll back to specific version in history

- To check the history of deployment

    `kubectl rollout history deployment/first-app`

- To go back to specific revision

    `kubectl rollout undo deployment/<dep-name> --to-revision=1`




