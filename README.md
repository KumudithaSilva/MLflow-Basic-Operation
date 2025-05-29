# Mlflow-Basic-Operation

# For Dagshub

import dagshub
dagshub.init(repo_owner='KumudithaSilva', repo_name='MLflow-Basic-Operation', mlflow=True)

import mlflow
with mlflow.start_run():
mlflow.log_param('parameter name', 'value')
mlflow.log_metric('metric name', 1)

export MLFLOW_TRACKING_URI=<DAGSHUB URL>
export MLFLOW_TRACKING_USERNAME=<DAGSHUB USERNAME>
export MLFLOW_TRACKING_PASSWORD=<<DAGSHUB PASSWORD>>

# For AWS

1. Login to AWS
2. Create IAM user with Admin
3. Export the credential in AWS CLI by running "aws configure"
4. Create a S3 bucket
5. Create EC2 and add security group 5000 port

# EC2 command

sudo apt update
sudo apt install python3-pip

pipx install pipenv
pipx install virtualenv

mkdir mlflow
cd mlflow

pipenv install mlflow
pipenv install awscli
pipenv install boto3

pipenv install shell

# AWS

aws config
mlflow server -h 0.0.0.0 --default-artifact-root s3://<S3 BUCKET NAME>

# Export In the Local environment

export MLFLOW_TRACKING_URI=https://<EC2_PUBLIC_DNS>.amazonaws.com:5000
