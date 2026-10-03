import os

from fastapi import FastAPI

SERVER_NAME = os.getenv("SERVER_NAME", "Unknown")


app = FastAPI(title=SERVER_NAME)

count = 0


@app.get("/")
def root():
    global count
    count += 1
    print("-" * 40)
    print("root endpoint reached")
    print(f"server: {SERVER_NAME}")
    print(f"Request count: {count}")
    return {
        "message": "Hello from FastAPI",
        "server": SERVER_NAME,
        "count": count,
    }


@app.get("/health")
def health():
    global count
    count += 1
    print("-" * 40)
    print("health endpoint reached")
    print(f"server: {SERVER_NAME}")
    print(f"Request count: {count}")
    return {
        "status": "healthy",
        "server": SERVER_NAME,
        "count": count,
    }
