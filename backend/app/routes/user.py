from fastapi import APIRouter, HTTPException, Query
from app.core.database import get_user, create_user, update_points

router = APIRouter(prefix="/user", tags=["User"])

@router.post("/register")
def register_user(email: str):
    created = create_user(email)
    if created:
        return {"status":"created","email":email}
    return {"status":"exists","email":email}

@router.get("/info")
def user_info(email: str = Query(...)):
    user = get_user(email)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@router.post("/use")
def user_use(email: str, points: int = 1):
    balance = update_points(email, points)
    if balance is None:
        raise HTTPException(status_code=404, detail="User not found")
    return {"status":"ok","balance":balance}
