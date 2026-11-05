
from fastapi import FastAPI

app = FastAPI()

# Endpoint 1: Welcome message
@app.get("/")
def home():
    return {"message": "Welcome to FastAPI"}

# Endpoint 2: Greeting with path parameter
@app.get("/greet/")
def greet(name: str):
    return {
        "message": f"Hello, {name}! Welcome to FastAPI."
    }
