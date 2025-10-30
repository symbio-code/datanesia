from fastapi import APIRouter, UploadFile, File, Form, HTTPException
from app.services.ai_summary import generate_summary_from_lux
from app.core.database import get_user, update_points, add_summary_log

router = APIRouter(prefix="/summary", tags=["Summary"])

@router.post("/local")
async def ai_summary_local(
    email: str = Form(...),
    category: str = Form(None),
    file: UploadFile = File(...)
):
    user = get_user(email)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    if not user.get("is_premium", False) and user.get("points", 0) < 3:
        raise HTTPException(status_code=402, detail="Not enough points")

    content = await file.read()
    result = generate_summary_from_lux(content, category)

    # save summary log
    add_summary_log(email, result["category"], result["narrative"], result["tags"])

    # deduct points if not premium
    if not user.get("is_premium", False):
        update_points(email, 3)

    updated_user = get_user(email)
    return {
        "status":"success",
        "category_used": result["category"],
        "summary": result["narrative"],
        "tags": result["tags"],
        "profiling": result["profiling"],
        "remaining_points": updated_user["points"]
    }
