### Working on the starting project for this Week

##### Start the container using docker compose file

        `docker compose up -d --build`

***Application can be tested using postman***


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