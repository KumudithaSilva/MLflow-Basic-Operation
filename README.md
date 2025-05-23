# Mlflow-Basic-Operation

# For Dagshub

import dagshub
dagshub.init(repo_owner='KumudithaSilva', repo_name='MLflow-Basic-Operation', mlflow=True)

import mlflow
with mlflow.start_run():
mlflow.log_param('parameter name', 'value')
mlflow.log_metric('metric name', 1)

export MLFLOW_TRACKING_URI=https://dagshub.com/KumudithaSilva/MLflow-Basic-Operation.mlflow
export MLFLOW_TRACKING_USERNAME=KumudithaSilva
export MLFLOW_TRACKING_PASSWORD=9a175a8613f271f255bb62cd240cb03a8e32c2e0
