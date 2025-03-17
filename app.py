from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def Read_root():
    return {"message": "Hello, FastAPI with linters!"}
