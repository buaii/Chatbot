from fastapi import FastAPI
import logging

app = FastAPI()

@app.get("/")
async def root():
    logging.info("root api run")
    return {"message": "Hello World"}