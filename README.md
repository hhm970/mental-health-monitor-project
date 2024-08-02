# Mental Health Monitor 🧠

## Introduction

Hi, and welcome to my solo-project for a data-driven mental-health monitor! The overall brand for this project is called _Mood For Thought_, and offers a dashboard, regular email-based notifications, and weekly PDF progress reports to help you gain a clearer headspace and greater overall wellbeing.


## Background & Problem Statement
**This project is designed to help users track and monitor their physical, emotional, and mental wellbeing.**

>The UK is going through a mental health crisis at the moment, with public mental health services being understaffed and in high demand. To mitigate the negative effects of bad mental health on individuals, we can use a data-driven pipeline-based tool.

## Requirements

### Prerequisites

- ```Python 3.11```
- `pip3`
- `awscli`
- `Docker`
- `Terraform`
- `PostgreSQL`

### Imports
Each sub-folder in this repository holds their own `requirements.txt` file. This is has been done to ensure clarity in what modules the scripts require.

In each folder's directory to download the requirements use this command:

```sh
pip3 install -r requirements.txt
  ```

**Secrets/Authentication**
> To be able to run these scripts locally the details must be provided in a `.env` file within each folder.
> Further details of the secrets required can be found in sub-folders `README.md`

## Cloud Deployment

## Directory Structure

This repository contains the following:

- `.github`: Contains code related to GitHub Actions and GitHub issues.

- `dashboard`: Contains code related to the dashboard.

- `database`: Contains code related to the deployment and setup of the database.

- `diagrams`: Contains `.png` files used to illustrate the infrastructure of the project.

- `pipeline`: Contains code related to the pipeline.

- `terraform`: Contains code which allows the AWS-based infrastructure to be setup via Terraform.

- `weekly_report`: Contains code which is related to the generation of the weekly report.


## Entity-Relationship Diagram
![ERD Diagram](<diagrams/erd.png>)

## Architecture Diagram
![Architecture Diagram](<diagrams/architecture.png>)

## Maintainers
[hhm970](https://github.com/hhm970)