from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Malicious IP Checker is alive!"}
