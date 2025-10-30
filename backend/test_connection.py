# ==========================================
# 📊 DataNesia - Supabase Connection Test
# ==========================================

from supabase import create_client
from dotenv import load_dotenv
import os

def test_connection():
    print("🔍 Testing Supabase connection...\n")

    # Baca file .env
    load_dotenv()

    SUPABASE_URL = os.getenv("SUPABASE_URL")
    SUPABASE_KEY = os.getenv("SUPABASE_KEY")

    # Validasi isi .env
    if not SUPABASE_URL or not SUPABASE_KEY:
        print("❌ Gagal: SUPABASE_URL atau SUPABASE_KEY belum diisi di .env")
        return

    print("✅ .env terbaca")
    print(f"   URL: {SUPABASE_URL}")
    print(f"   KEY: {SUPABASE_KEY[:8]}... (disembunyikan)\n")

    try:
        # Buat client
        supabase = create_client(SUPABASE_URL, SUPABASE_KEY)

        # Tes query ke tabel users_points
        response = supabase.table("users_points").select("*").execute()

        print("✅ Koneksi Supabase berhasil!")
        print(f"   Jumlah data di tabel users_points: {len(response.data)}")
        print("   Contoh isi data:", response.data[:1])
    except Exception as e:
        print("❌ Error saat koneksi:", e)

if __name__ == "__main__":
    test_connection()
