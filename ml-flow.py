import mlflow
import dagshub
from mlflow.models import infer_signature
from mlflow.client import MlflowClient

import pandas as pd
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score

# Load the Iris dataset
X, y = datasets.load_iris(return_X_y=True)

# Split the data into training and test sets
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Define the model hyperparameters
params = {
    "solver": "liblinear",     
    "C": 1.0,                 
    "penalty": "l2",          
    "max_iter": 300,           
    "random_state": 8888,
}

# Train the model
lr = LogisticRegression(**params)
lr.fit(X_train, y_train)

# Predict on the test set
y_pred = lr.predict(X_test)

# Calculate metrics
accuracy = accuracy_score(y_test, y_pred)
# =====================================================================

# Set dagshub configuration
dagshub.init(repo_owner='KumudithaSilva', repo_name='MLflow-Basic-Operation', mlflow=True)

# Set our tracking server uri for logging
remort_server_uri = "https://dagshub.com/KumudithaSilva/MLflow-Basic-Operation.mlflow"
mlflow.set_tracking_uri(remort_server_uri)

# Create a new MLflow Experiment
mlflow.set_experiment("MLflow Logistic Regression")

# Start an MLflow run
with mlflow.start_run() as run:
    run_id = run.info.run_id
    # Log the hyperparameters
    mlflow.log_params(params)

    # Log the loss metric
    mlflow.log_metric('accuracy', accuracy)

    # Set a tag that we can use to remind ourselves what this run was for
    mlflow.set_tag("Traning Info", "Basic Logistic Regression for iris dataset.")

    # Infer the model signature
    signature = infer_signature(X_train, lr.predict(X_train))

    # Log the model
    model_info = mlflow.sklearn.log_model(
        sk_model = lr,
        artifact_path = 'iris_model',
        input_example = X_train,
        registered_model_name = "traning-quickstart"
    )

#======================================================
# Load the model back for predictions as a generic Python Function model
loaded_model = mlflow.pyfunc.load_model(model_info.model_uri)

predictions = loaded_model.predict(X_test)


iris_feature_names = datasets.load_iris().feature_names

result = pd.DataFrame(X_test, columns=iris_feature_names)
result["actual_class"] = y_test
result["predicted_class"] = predictions

result[:4]

#======================================================
# Create source model version
client = MlflowClient()
src_name = "LogisticRegression3-staging"
client.create_registered_model(src_name)
src_uri = f"runs:/{run_id}/sklearn-model"
mv_src = client.create_model_version(src_name, src_uri, run.info.run_id)

# Copy the source model version into a new registered model
dst_name = "LogisticRegression3-production"
src_model_uri = f"models:/{mv_src.name}/{mv_src.version}"
mv_copy = client.copy_model_version(src_model_uri, dst_name)
