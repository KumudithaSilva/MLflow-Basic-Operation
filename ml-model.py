from mlflow import MlflowClient
import mlflow
import dagshub

dagshub.init(repo_owner='KumudithaSilva', repo_name='MLflow-Basic-Operation', mlflow=True)

# Set our tracking server uri for logging
remort_server_uri = "https://dagshub.com/KumudithaSilva/MLflow-Basic-Operation.mlflow"
mlflow.set_tracking_uri(remort_server_uri)

client = MlflowClient()
client.transition_model_version_stage(
    name="traning-quickstart", version=2, stage="Production"
)
