import os
import socket

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def root():
    return {
        "message": "Hello from FastAPI",
        "instance": os.getenv("INSTANCE_NAME", "unknown"),
        "hostname": socket.gethostname(),
        "pid": os.getpid(),
    }


@app.get("/health")
def health():
    return {"status": "ok"}
