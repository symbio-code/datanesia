import pandas as pd
import lux
import tempfile, os
from app.core.utils import parse_csv_bytes

def generate_lux_recommendations(file_content: bytes, max_charts=5):
    temp_path = tempfile.NamedTemporaryFile(delete=False, suffix=".csv").name
    with open(temp_path, "wb") as f:
        f.write(file_content)
    df = pd.read_csv(temp_path)
    try:
        df._repr_html_()
        recs = getattr(df, "recommendation", {})
        charts = []
        for cat in recs:
            actions = recs[cat].get("action", [])
            for vis in actions:
                try:
                    charts.append({
                        "action": cat,
                        "description": recs[cat].get("description", ""),
                        "chart_code": str(vis.to_code("matplotlib"))
                    })
                except Exception:
                    continue
            if len(charts) >= max_charts:
                break
    except Exception:
        charts = []
    finally:
        os.remove(temp_path)
    return charts[:max_charts]
