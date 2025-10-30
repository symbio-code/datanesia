from fastapi import APIRouter
from app.core.config import supabase

router = APIRouter(prefix="/payment", tags=["Payment"])

@router.post("/success")
async def payment_success(payload: dict):
    email = payload.get("email")
    plan = payload.get("plan", "topup")
    amount = payload.get("amount", 0)

    if plan == "premium":
        supabase.table("users_points").update({"plan":"premium","points":9999}).eq("email", email).execute()
    else:
        # use rpc increment_points if defined
        try:
            supabase.rpc("increment_points", {"email_input": email, "add_points": 20}).execute()
        except Exception:
            supabase.table("users_points").update({"points": supabase.raw("points + 20")}).eq("email", email).execute()

    supabase.table("payments").insert({
        "email": email,
        "amount": amount,
        "plan": plan,
        "status":"success"
    }).execute()
    return {"status":"ok"}
