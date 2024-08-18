
### Environment variables

- Environment variable can be declared:
        
        -- Configure the variable in the deployment.yaml file

                ```
                        In the containers config:
                        below image name:
                        env:
                          - name: VARIABLE_NAME
                            value: 'value'
                ```

- It can be used depending on the syntax of language being used.


#### Environment Variable using Config Maps

        Instead of tying down environment variable to one deployment, We can create config maps
        which multiple deployment/pods can access and use.

        - Config Map is an object of kubernetes which creates a key, value list pairs.

        1. Write a yaml configuration for config maps
        2. Configure the deployment to take values from config map


            `kubectl apply -f env.yaml`
            `kubectl get configmap`