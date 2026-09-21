import os

from fastapi import FastAPI

SERVER_NAME = os.getenv("SERVER_NAME", "UNKNOWN")
ROOT_PATH = os.getenv("ROOT_PATH", "/")

app = FastAPI(title=SERVER_NAME, root_path=ROOT_PATH)


@app.get("/")
def root():
    return {"message": f"Hello from {SERVER_NAME}"}


@app.get("/health")
def health():
    return {"status": "ok", "message": f"Hello from {SERVER_NAME}"}
