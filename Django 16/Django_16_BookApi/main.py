from fastapi import FastAPI

app = FastAPI(title="BookApi")

@app.get("/")
async def root():
    return {"message": "Hello World"}