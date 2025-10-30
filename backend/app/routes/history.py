from fastapi import APIRouter
from app.core.config import supabase

router = APIRouter(prefix="/history", tags=["History"])

@router.get("/")
def get_history(email: str = None):
    q = supabase.table("summary_logs").select("*")
    if email:
        q = q.eq("email", email)
    res = q.execute()
    return res.data
