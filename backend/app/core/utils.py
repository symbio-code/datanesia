import pandas as pd
from io import BytesIO

def parse_csv_bytes(content: bytes):
    try:
        return pd.read_csv(BytesIO(content))
    except Exception:
        # fallback to excel
        import io
        return pd.read_excel(io.BytesIO(content))
