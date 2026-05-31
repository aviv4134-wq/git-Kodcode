from fastapi import FastAPI
import uvicorn
app = FastAPI()
import requests


@app.get('/ping')
def get_status():
    return {'status':'pong'}

@app.get('/greet/{name}')
def greet(name:str):
   return {"message": f"Hello, {name}!"}



