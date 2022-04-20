import tempfile
import joblib
import typing as t
import pandas as pd

from fastapi import FastAPI, Depends, Body
from pydantic import BaseSettings
from functools import lru_cache
from entities import ModelInput
from boto3 import client


app = FastAPI(title="Breast Cancer classifier API", version="1.0.0")

class Settings(BaseSettings):
  aws_region: str
  aws_access_key_id: str
  aws_secret_access_key: str
  class Config:
    env_file = '.env'
    env_file_encoding = 'utf-8'

@lru_cache(None)
def get_settings():
  return Settings()

@lru_cache(None)
def load_estimator():
  with tempfile.TemporaryFile() as fp:
    clientS3 = get_client()
    clientS3.download_fileobj(Fileobj=fp, Bucket='camilo-ml-models-bucket', Key='models/model.joblib')
    fp.seek(0)
    model = joblib.load(fp)
    return model

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

def get_client():
  settings = get_settings()
  clientS3 = client(
    's3',
    aws_access_key_id=settings.aws_access_key_id,
    aws_secret_access_key=settings.aws_secret_access_key
  )
  return clientS3

if __name__ == "__main__":
  import uvicorn
  uvicorn.run(app)