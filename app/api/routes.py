from fastapi import APIRouter, UploadFile, File
from app.services.analysis import analyze_csv

router = APIRouter()

@router.post("/analyze")
async def analyze(file: UploadFile = File(...)):
    result = analyze_csv(file)
    return result
