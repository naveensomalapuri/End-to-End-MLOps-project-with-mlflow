import setuptools

with open("README.md", "r", encoding="utf") as f:
    long_description = f.read()

__version__ = "0.0.0"

REPO_NAME = "End-to-end-ML-Project-with-MLflow"
AUTHOR_USER_NAME = "Somalapuri Naveen"
SRC_REPO = "mlProject"
AUTHOR_EMAIL = "somalapurinaveen@gmail.com"

setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="A small python package for ml app",
    long_description=long_description,
    url=f"https://github.com/naveensomalapuri/End-to-End-MLOps-project-with-mlflow",
    project_url={
        "Bug Tracker" : f"https://github.com/naveensomalapuri/End-to-End-MLOps-project-with-mlflow/issues",
    },
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src")
)