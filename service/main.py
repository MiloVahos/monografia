from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def service_status():
  """Check the status of the service"""
  return {"status": "ok"}

@app.post("/")
async def make_prediction():
  return {"prediction": "ok"}

if __name__ == "__main__":
  import uvicorn
  uvicorn.run(app)