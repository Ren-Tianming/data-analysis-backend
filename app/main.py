from fastapi import FastAPI
from app.api.routes import router

app = FastAPI(title="Data Analysis API")

app.include_router(router)

@app.get("/")
def root():
    return {"message": "Data Analysis Backend is running"}
