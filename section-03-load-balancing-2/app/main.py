import asyncio as asyn
import os
import socket
from pathlib import Path

from fastapi import FastAPI, HTTPException, Query

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


@app.get("/work")
async def work(delay: float = Query(ge=0, le=10, default=0)):
    await asyn.sleep(delay)
    return {
        "instance": os.getenv("INSTANCE_NAME", "unknown"),
        "delay": delay,
        "hostname": socket.gethostname(),
        "pid": os.getpid(),
    }


NOT_READY_FILE = Path("/tmp/nginx-lab-not-ready")


@app.get("/health/live")
async def liveness():
    return {
        "status": "alive",
        "instance": os.getenv("INSTANCE_NAME", "unknown"),
    }


@app.get("/health/ready")
async def readiness():
    if NOT_READY_FILE.exists():
        raise HTTPException(
            status_code=503,
            detail="Instance is not ready",
        )

    return {
        "status": "ready",
        "instance": os.getenv("INSTANCE_NAME", "unknown"),
    }


@app.get("/simulate/error")
async def simulate_error():
    raise HTTPException(
        status_code=500,
        detail="Simulated application error",
    )


@app.get("/simulate/unavailable")
async def simulate_unavailable():
    raise HTTPException(
        status_code=503,
        detail="Simulated service unavailability",
    )


@app.get("/{path:path}")
async def catch_all(path: str):
    return {
        "path": path,
        "instance": os.getenv("INSTANCE_NAME", "unknown"),
        "hostname": socket.gethostname(),
        "pid": os.getpid(),
    }
