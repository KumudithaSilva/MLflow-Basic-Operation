# MLflow Basic Operation

A simple guide to set up and use **MLflow** tracking with both **DagsHub** and **AWS**.

---

## 🚀 Getting Started

This repository demonstrates how to log parameters and metrics with MLflow using two setups:

- **DagsHub** (for easy cloud tracking)
- **AWS** (for a custom MLflow server on EC2 with S3 artifact storage)

---

## 🔧 Setup for DagsHub

1. Initialize your repo with DagsHub's MLflow integration:
   ```python
   import dagshub
   dagshub.init(repo_owner='KumudithaSilva', repo_name='MLflow-Basic-Operation', mlflow=True)

2. Example MLflow logging
   ```python
   import mlflow
   with mlflow.start_run():
   mlflow.log_param('parameter_name', 'value')
   mlflow.log_metric('metric_name', 1)
      
3. Set environment variables to connect MLflow CLI or SDK to DagsHub:
    ```bash
    export MLFLOW_TRACKING_URI=<DAGSHUB_URL>
    export MLFLOW_TRACKING_USERNAME=<DAGSHUB_USERNAME>
    export MLFLOW_TRACKING_PASSWORD=<DAGSHUB_PASSWORD>


## ☁️ Setup for AWS

### Step 1: Prepare AWS

- Login to AWS Console.
- Create an IAM user with **AdministratorAccess**.
- Configure AWS CLI credentials locally by running:

    ```bash
    aws configure
    ```

- Create an S3 bucket for MLflow artifacts.
- Launch an EC2 instance with a security group allowing inbound traffic on port **5000**.

---

### Step 2: EC2 Environment Setup

Connect to your EC2 instance and run the following commands to install dependencies and set up your environment:

```bash
sudo apt update
sudo apt install -y python3-pip

pipx install pipenv
pipx install virtualenv

mkdir mlflow
cd mlflow

pipenv install mlflow awscli boto3
pipenv shell
```

---

### Step 3: Run MLflow Server

Start the MLflow tracking server on your EC2 instance, specifying the S3 bucket as the default artifact storage location:

```bash
mlflow server --host 0.0.0.0 --default-artifact-root s3://<S3_BUCKET_NAME> --port 5000
```

### Step 4: Export Local Environment

```bash
export MLFLOW_TRACKING_URI=http://<EC2_PUBLIC_DNS>:5000
```
