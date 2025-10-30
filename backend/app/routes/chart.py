from fastapi import APIRouter, UploadFile, File
from app.services.ai_chart import generate_lux_recommendations

router = APIRouter(prefix="/chart", tags=["Chart"])

@router.post("/lux")
async def chart_lux(file: UploadFile = File(...)):
    content = await file.read()
    charts = generate_lux_recommendations(content)
    return {"model":"lux","charts":charts}
