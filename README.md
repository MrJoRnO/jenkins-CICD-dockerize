# Mission 1: Simple Deployment Pipeline

## Objective
This project implements an efficient Jenkins CI/CD pipeline designed to automate the lifecycle of a Dockerized application. The goal is to ensure a consistent and reliable workflow from source code to production. 

## Pipeline Workflow
The pipeline consists of three main stages:

1. **Build Docker Image**: Automatically builds a Docker image from the application source code using a unique version tag for tracking. 
2. **Tag & Push**: Tags the image appropriately and pushes it to a DockerHub repository for centralized management and accessibility. 
3. **Ansible Deployment**: Executes an Ansible playbook (`deploy-playbook.yml`) to deploy the application container to the target environment. 



## Prerequisites
* **Jenkins** installed with Docker and Ansible plugins.
* **DockerHub** account and credentials configured in Jenkins.
* **Ansible** installed on the Jenkins agent.
* A valid `Dockerfile` and `deploy-playbook.yml` in the root directory.

## Getting Started
1. Clone this repository to your local machine.
2. Configure your DockerHub credentials in Jenkins with the ID `dockerhub-credentials-id`.
3. Create a new "Pipeline" job in Jenkins and point it to the `Jenkinsfile` in this repo.
4. Run the build.

## Outcome
A fully automated, streamlined pipeline that minimizes manual intervention and ensures a professional deployment standard. 