from functools import lru_cache
from sklearn.base import BaseEstimator
from datetime import datetime, timezone

import data
import model

import os
import typer
import yaml
import joblib
import shutil
import pandas as pd
import typing as t

# This is a way to create CLI
app = typer.Typer()

class CsvDatasetReader:
  # Replace the initializer of the function with the code inside
  def __init__(self, filepath: str) -> None:
    self.filepath = filepath
  
  # Allows to use the class a function, when calling an instance of the class
  def __call__(self):
    return _read_csv(self.filepath)


@app.command()
def train(config_file: str):
  hyperparams = _load_config(config_file, "hyperparams")
  split = "train"
  X, y = _get_dataset(_load_config(config_file, "data"), splits=[split])[split] 
  estimator = model.build_estimator(hyperparams)
  estimator.fit(X, y)
  output_dir = _load_config(config_file, "export")["output_dir"]
  version = _save_versioned_estimator(estimator, hyperparams, output_dir)
  return version

@app.command()
def hello(name: str):
  typer.echo(f"Hello {name}")

@lru_cache(None) # This is some kind of memoize cache
def _read_csv(filepath):
  return pd.read_csv(filepath)

def _load_config(filepath: str, key: str):
  content = _load_yaml(filepath)
  config = content[key]
  return config

@lru_cache(None)
def _load_yaml(filepath: str) -> t.Dict[str, t.Any]:
  # Load the yaml file into the yaml object
  with open(filepath, "r") as f:
    content = yaml.safe_load(f)
    return content

def _get_dataset(data_config, splits):
  filepath = data_config["filepath"]
  reader = CsvDatasetReader(filepath)
  return data.get_dataset(reader=reader, splits=splits)

def _save_yaml(content: t.Dict[str, t.Any], filepath: str):
  with open(filepath, "w") as f:
    yaml.dump(content, f)

def _save_versioned_estimator(estimator: BaseEstimator, hyperparams: t.Dict[str, t.Any], output_dir: str):
  version = str(datetime.now(timezone.utc).replace(second=0, microsecond=0))
  model_dir = os.path.join(output_dir, version)
  os.makedirs(model_dir, exist_ok=True)
  try:
    joblib.dump(estimator, os.path.join(model_dir, "model.joblib"))
    _save_yaml(hyperparams, os.path.join(model_dir, "params.yml"))
  except Exception as e:
    typer.echo(f"Coudln't serialize model due to error {e}")
    shutil.rmtree(model_dir)
  return version

if __name__ == "__main__":
  # the CLI app will be called when calling the module
  app()