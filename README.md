# CI/CD Pipeline for Microservice Application

## Project Overview

This project demonstrates a complete CI/CD pipeline implementation using **GitHub Actions** and **OpenShift Tekton Pipelines** for a Python Flask microservice application.

## Technologies Used

- **Python / Flask** — Microservice backend
- **GitHub Actions** — Continuous Integration (lint + unit tests)
- **Tekton Pipelines** — Continuous Delivery on OpenShift
- **OpenShift** — Container platform for deployment
- **flake8** — Python linting
- **nose** — Python unit testing
- **Docker / Buildah** — Container image building

## Pipeline Stages

### GitHub Actions (CI)
1. Lint with flake8
2. Run unit tests with nose

### Tekton Pipeline (CD)
1. Cleanup workspace
2. Clone repository
3. Lint code
4. Run tests with nose
5. Build Docker image
6. Deploy to OpenShift

## Repository Structure

```
.
├── .github/
│   └── workflows/
│       └── workflow.yml       # GitHub Actions CI workflow
├── .tekton/
│   └── tasks.yml              # Tekton pipeline tasks
├── service/
│   ├── __init__.py
│   ├── models.py
│   └── routes.py
├── tests/
│   ├── __init__.py
│   └── test_routes.py
├── requirements.txt
├── setup.cfg
└── README.md
```

## Running Locally

```bash
pip install -r requirements.txt
flake8 service tests --count --max-complexity=10 --max-line-length=127
nosetests -v --with-spec --spec-color
```

## OpenShift Deployment

```bash
oc apply -f .tekton/tasks.yml
oc create -f .tekton/pipeline-run.yml
```
