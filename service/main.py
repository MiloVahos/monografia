import sys
import joblib
import typing as t
import pandas as pd

from fastapi import FastAPI, Depends, Body
from pydantic import BaseSettings
from functools import lru_cache
from entities import ModelInput

app = FastAPI(title="Breast Cancer classifier API", version="1.0.0")

class Settings(BaseSettings):
  serialized_model_path: str
  model_lib_dir: str

@lru_cache(None)
def get_settings():
  return Settings()

@lru_cache(None)
def load_estimator():
  sys.path.append('modelling')
  estimator = joblib.load('/Users/camilovahos/Desktop/LEARNING/SPEC/Monografia/Monografia/modelling/models/2022-03-23 00:30:00+00:00/model.joblib')
  return estimator

@app.get("/")
async def service_status():
  """Check the status of the service"""
  return {"status": "ok"}

@app.post("/", response_model=t.List[str])
async def make_prediction(
  inputs: t.List[ModelInput] = Body(...),
  estimator=Depends(load_estimator)
):
  X = pd.DataFrame([row.dict() for row in inputs])
  print('here')
  prediction = estimator.predict(X).tolist()
  print(prediction)
  return prediction

if __name__ == "__main__":
  import uvicorn
  uvicorn.run(app)