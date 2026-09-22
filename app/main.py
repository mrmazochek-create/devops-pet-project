from fastapi import FastAPI
from fastapi.responses import JSONResponse
import os
import socket

app = FastAPI(title="DevOps Pet Project")

@app.get("/")
async def root():
    return {
        "message": "Hello DevOps!",
        "service": "devops-pet-project",
        "version": "1.0.0"
    }

@app.get("/health")
async def health():
    return {
        "status": "healthy",
        "hostname": socket.gethostname()
    }

@app.get("/ready")
async def ready():
    return {"status": "ready"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8080)
