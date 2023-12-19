# End-to-End-MLOps-project-with-mlflow



## Workflows

1. Update config.yaml
2. Update schema.yaml
3. Update params.yaml
4. Update the entity
5. Update the configuration manager in src config
6. Update the components
7. Update the pipeline
8. Update the main.py
9. Update the app.py


# How to run?

### STEPS:
Clone the repository

```bash
https://github.com/somalapurinaveen/End-to-End-MLOps-project-with-mlflow

```

### STEP 01- Create a conda environment after opening the repository

```bash
conda create -n mlproj python=3.8 -y
```

```bash
conda activate mlproj
```

### STEP 02- install the requirements
```bash
pip install -r requirements.txt
```
Now,
```bash
open up you local host and port
```

## MLflow

[Documentation](https://mlflow.org/docs/latest/index.html)

#### cmd
-mlflow ui

### dagshub
[dagshub](https://dagshub.com/)

MLFLOW_TRACKING_URI=https://dagshub.com/somalapurinaveen/End-to-End-MLOps-project-with-mlflow.mlflow \
MLFLOW_TRACKING_USERNAME=somalapurinaveen \
MLFLOW_TRACKING_PASSWORD=c170b1e9277f3c97f68a2a650473087caf3645af \
python script.py

Run this to export as env variables:

```bash
export MLFLOW_TRACKING_URI=https://dagshub.com/somalapurinaveen/End-to-End-MLOps-project-with-mlflow.mlflow 

export MLFLOW_TRACKING_USERNAME = somalapurinaveen

export MLFLOW_TRACKING_PASSWORD=c170b1e9277f3c97f68a2a650473087caf3645af 

```