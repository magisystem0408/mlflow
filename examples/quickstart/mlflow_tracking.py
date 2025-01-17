import os

from mlflow import log_artifacts, log_metric, log_param
import secrets

if __name__ == "__main__":
    print("Running mlflow_tracking.py")

    log_param("param1", secrets.SystemRandom().randint(0, 100))

    log_metric("foo", secrets.SystemRandom().random())
    log_metric("foo", secrets.SystemRandom().random() + 1)
    log_metric("foo", secrets.SystemRandom().random() + 2)

    if not os.path.exists("outputs"):
        os.makedirs("outputs")
    with open("outputs/test.txt", "w") as f:
        f.write("hello world!")

    log_artifacts("outputs")
