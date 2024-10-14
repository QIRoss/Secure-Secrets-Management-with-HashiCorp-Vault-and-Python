# Secure Secrets Management with HashiCorp Vault and Python

Studies based in day 55-56 of 100 Days System Design for DevOps and Cloud Engineers.

https://deoshankar.medium.com/100-days-system-design-for-devops-and-cloud-engineers-18af7a80bc6f

Days 51–60: Security and Compliance at Scale

Day 55–56: Set up and manage a Vault cluster for secrets management at scale.

## Project Overview

This project is centered around setting up and managing a HashiCorp Vault cluster for secure secrets management. Vault is a highly secure tool that allows centralized storage, access control, and auditing of sensitive information such as API keys, passwords, certificates, and encryption keys.

By using Vault, you ensure that secrets are encrypted both at rest and in transit, with fine-grained access control policies that allow only authorized users and applications to retrieve secrets. Additionally, Vault offers dynamic secret generation, allowing on-demand credentials (e.g., database logins) with automatic expiration and revocation. This minimizes the risk of credential exposure and enhances overall security compliance.

### Recommended Use of SSL in Production

In any production environment, using SSL/TLS (HTTPS) is critical for securing communication between Vault and client applications. Without SSL, secrets and credentials could be exposed during transmission, especially in cloud or distributed systems where traffic could traverse public networks.

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