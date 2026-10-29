import asyncio as asyn
import os
import socket

from fastapi import FastAPI, Query

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


@app.get("/{path:path}")
async def catch_all(path: str):
    return {
        "path": path,
        "instance": os.getenv("INSTANCE_NAME", "unknown"),
        "hostname": socket.gethostname(),
        "pid": os.getpid(),
    }
