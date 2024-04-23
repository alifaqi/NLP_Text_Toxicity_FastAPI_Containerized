from fastapi import FastAPI
from apps import read_comments

app = FastAPI()

@app.get("/")
async def root():
    return read_comments()
