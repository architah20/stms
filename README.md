# STMS - Student Task Management System

Course: Agile Software Development and DevOps
One Flask app taken through the full DevOps lifecycle (all 9 experiments).

**Flow:** Jira -> Git/GitHub -> (Jenkins | GitHub Actions) -> Docker -> AWS EC2 -> Prometheus/Grafana
**Infra:** Terraform provisions the AWS server.

| Exp | Topic | Where in this repo |
|---|---|---|
| 1 | Git operations | `docs/GIT_COMMANDS.md`, commit/branch/PR history |
| 2 | Docker | `Dockerfile` |
| 3 | Docker Compose | `docker-compose.yml` |
| 4 | Jenkins CI | `Jenkinsfile`, `docker-compose.jenkins.yml`, `jenkins/` |
| 5 | Automated deployment | `.github/workflows/ci.yml`, `Jenkinsfile` |
| 6 | Jira + DevOps integration | Jira board `STMS`, `docs/jira-backlog.csv` |
| 7 | Monitoring | `prometheus/`, `grafana/` |
| 8 | CI/CD to AWS | `deploy` job in `ci.yml` |
| 9 | Terraform on AWS | `terraform/` |

## Run locally (no Docker)
    pip install -r requirements.txt
    python app/app.py            # http://localhost:5000
    cd app && pytest -v          # run tests

## Run everything with Docker Compose
    docker compose up -d --build
    App         http://localhost:5000
    Prometheus  http://localhost:9090   (Status > Targets)
    Grafana     http://localhost:3000   (admin / admin) -> dashboard "STMS Monitoring"
    docker compose down

## Features
Add / rename / complete / delete tasks, due date, priority, `/health`, `/metrics`, `/api/tasks`.

## System Architecture

The Student Task Management System follows a simple DevOps workflow:

Development: Developers write Python Flask application code and manage changes using Git.

Version Control: GitHub stores the source code, branches, commits, and pull requests.

Continuous Integration: Jenkins and GitHub Actions automate application testing.

Containerization: Docker packages the Flask application into a portable container.

Orchestration: Docker Compose runs the application and monitoring services together.

Deployment: The application can be deployed to an AWS EC2 instance using the CI/CD workflow.

Infrastructure as Code: Terraform defines the AWS infrastructure configuration.

Monitoring: Prometheus collects application metrics, while Grafana visualizes them.

## Application Endpoints

Endpoint

Purpose

/

View and manage tasks

/health

Check application health

/api/tasks

Retrieve tasks in JSON format

/metrics

Expose metrics for Prometheus

## Development Workflow

Create a feature branch, implement a change, run the automated tests, commit the changes, push the branch to GitHub, and open a Pull Request targeting main. After reviewing and merging the Pull Request, synchronize the local main branch.

## Testing

Run the automated test suite from the project root:

python -m pytest -v

The tests cover application health, homepage loading, task creation, task completion and deletion, metrics availability, and task priority validation.
