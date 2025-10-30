from fastapi import APIRouter, UploadFile, File
from app.core.utils import parse_csv_bytes

router = APIRouter(prefix="/upload", tags=["Upload"])

@router.post("/")
async def upload_preview(file: UploadFile = File(...)):
    content = await file.read()
    df = parse_csv_bytes(content)
    return {
        "columns": list(df.columns),
        "preview": df.head(5).to_dict(orient="records"),
        "rows": len(df)
    }
