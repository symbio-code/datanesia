from app.core.config import supabase

import os

# TinyDB local (optional) — keep small cache

# TinyDB optional (disabled for now)
tinydb = None
User = None


# Supabase helpers
def get_user(email: str):
    res = supabase.table("users_points").select("*").eq("email", email).execute()
    return res.data[0] if res.data else None

def create_user(email: str):
    if get_user(email):
        return False
    supabase.table("users_points").insert({
        "email": email,
        "points": 20,
        "plan": "free"
    }).execute()
    return True

def update_points(email: str, used_points: int):
    user = get_user(email)
    if not user:
        return None
    new_points = max(0, user["points"] - used_points)
    supabase.table("users_points").update({"points": new_points}).eq("email", email).execute()
    return new_points

def add_summary_log(email: str, category: str, summary: str, tags: list):
    supabase.table("summary_logs").insert({
        "email": email,
        "category": category,
        "summary": summary,
        "tags": tags
    }).execute()
