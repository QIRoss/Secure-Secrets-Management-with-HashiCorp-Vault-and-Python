# Secure Secrets Management with HashiCorp Vault and Python

Studies based in day 55-56 of 100 Days System Design for DevOps and Cloud Engineers.

https://deoshankar.medium.com/100-days-system-design-for-devops-and-cloud-engineers-18af7a80bc6f

Days 51–60: Security and Compliance at Scale

Day 55–56: Set up and manage a Vault cluster for secrets management at scale.

## Project Overview

### How to run

```
docker-compose up --build
```

Open another terminal
```
docker exec -it vault sh
vault login root
vault secrets enable -path=secret kv-v2
vault kv put secret/mysecret password="supersecretpassword"
``` 

Go to ```http://localhost:8000/secret/mysecret``` and check your password.

## Author
This project was implemented by [Lucas de Queiroz dos Reis][2]. It is based on the [100 Days System Design for DevOps and Cloud Engineers][1].

[1]: https://deoshankar.medium.com/100-days-system-design-for-devops-and-cloud-engineers-18af7a80bc6f "Medium - Deo Shankar 100 Days"
[2]: https://www.linkedin.com/in/lucas-de-queiroz/ "LinkedIn - Lucas de Queiroz"