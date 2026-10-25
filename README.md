# MyProjects — Multi-Domain Infrastructure, DevOps & Python Engineering Collection

A curated personal collection of Infrastructure-as-Code (IaC), configuration management playbooks, AWS operational automation utilities, and Python exercises developed between 2016 and 2026.

---

## Repository Directory Index

| Directory | Domain | Key Contents & Purpose |
|---|---|---|
| [`Ansible/`](Ansible/) | Configuration Management | Multi-tier production & staging Ansible architecture with 12 roles (`common`, `nginx`, `haproxy`, `mysql`, `mongodb`, `rabbitmq`, `memcached`, `tomcat`, `java`, `frontends`, `backends`, `users-init`). |
| [`Terraform/`](Terraform/) | Infrastructure as Code | Reusable AWS Terraform modules for EC2 instance provisioning (`modules/ec2_instance`) and Amazon ECS cluster + autoscaling group setup (`modules/ecs`). |
| [`DevOps-scripts-master/`](DevOps-scripts-master/) | Cloud & Ops Automation | AWS CLI / Boto operational scripts for Route53 DNS record automation, S3 bucket inspection, EC2 tag-triggered deployments, and Tomcat JMX cluster monitoring (`tomcats/`). |
| [`Python/`](Python/) | Python Projects | Interactive Python applications and algorithmic exercises, including a CLI Hangman game (`Python/Hangman`) and an arcade Pong implementation (`Python/Pong`). |
| [`Examples/`](Examples/) | Reference Snippets | Standalone Python reference scripts (`1.py`, `2.py`, `guess_game.py`). |

---

## Usage & Security Notes

- **Inventory & Variable Sanitization:** All example inventories (`Ansible/production/inventory`, `Ansible/staging/inventory`) and Terraform variable defaults (`Terraform/modules/*/vars.tf`) use RFC 5737 documentation IP ranges (`192.0.2.0/24`, `198.51.100.0/24`) and placeholder AWS resource identifiers (`vpc-00000000example`). Override them via environment variables or untracked `*.tfvars` files.
- **State Files:** Terraform `.tfstate` files, SSH keys (`*.pem`), and Ansible `.retry` artifacts are excluded via `.gitignore`.
