from fastapi import APIRouter, Header, HTTPException
from app.core.config import supabase
from app.core.database import create_user

router = APIRouter(prefix="/auth", tags=["Auth"])

@router.post("/sync")
async def sync_user(authorization: str = Header(...)):
    if " " not in authorization:
        raise HTTPException(status_code=400, detail="Authorization header malformed")
    token = authorization.split(" ")[1]
    res = supabase.auth.get_user(token)
    user = res.user if hasattr(res, "user") else None
    if not user:
        raise HTTPException(status_code=401, detail="Invalid token")
    email = user.email
    create_user(email)
    return {"status":"ok","email":email}
