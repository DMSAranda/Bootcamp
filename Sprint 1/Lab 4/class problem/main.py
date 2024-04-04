from fastapi import FastAPI
from datetime import datetime

app = FastAPI()

@app.get("/")

def read_root():
    return {
            "message: Welcome API"
           }



@app.get("/greeting/{name}")

def greeting(name: str):
    date = datetime.now().strftime("%Y-%m-%d %H:%M")
    return {
            "message": f"Hi {name}, today is {date}"
           }



@app.get("/lenText/{text}")

def lenText(text: str):
    return {
            "text": text,
            "length": len(text)
           }