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
  class Config:
    env_file = '.env'
    env_file_encoding = 'utf-8'

@lru_cache(None)
def get_settings():
  return Settings()

@lru_cache(None)
def load_estimator():
  sys.path.append(get_settings().model_lib_dir)
  estimator = joblib.load(get_settings().serialized_model_path)
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
  prediction = estimator.predict(X).tolist()
  return prediction

if __name__ == "__main__":
  import uvicorn
  uvicorn.run(app)