import pandas as pd
import tempfile, os
from ydata_profiling import ProfileReport
from pandasai import PandasAI
from pandasai.llm.local_llm import LocalLLM
from app.core.config import AI_API_KEY
from app.core.detector import detect_dataset_category
from app.core.utils import parse_csv_bytes
from supabase import create_client
import json

try:
    import openai
except Exception:
    openai = None

def generate_summary_from_lux(file_content: bytes, category: str = None):
    df = parse_csv_bytes(file_content)

    if not category:
        category = detect_dataset_category(df)

    # Basic stats
    overview = {
        "rows": len(df),
        "columns": len(df.columns),
    }

    # Compose prompt template per category
    prompts = {
        "sales": "You are a sales analyst... (English + Bahasa Indonesia). Provide Overview, TopPerformers, Trend, Highlight, Narrative, Recommendation.",
        "marketing": "You are a marketing analyst... (English + Bahasa Indonesia). Provide Overview, TopPerformers, Trend, Highlight, Narrative, Recommendation.",
        "finance": "You are a finance analyst... (English + Bahasa Indonesia). Provide Overview, TopPerformers, Trend, Highlight, Narrative, Recommendation.",
        "saas": "You are a SaaS analyst... (English + Bahasa Indonesia). Provide Overview, TopPerformers, Trend, Highlight, Narrative, Recommendation.",
        "general": "You are a data analyst... Provide Overview, Trend, Highlight, Narrative."
    }
    selected_prompt = prompts.get(category, prompts["general"])

    # Local attempt via PandasAI
    try:
        llm = LocalLLM()
        pandas_ai = PandasAI(llm)
        narrative = pandas_ai.run(df, selected_prompt)
    except Exception as e:
        narrative = f"PandasAI local unavailable ({e})"

    # Fallback to OpenAI if configured
    if openai and AI_API_KEY:
        try:
            openai.api_key = AI_API_KEY
            res = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[{"role": "user", "content": selected_prompt + "\n\nDataframe columns: " + ", ".join(df.columns)}],
                temperature=0.7,
            )
            narrative = res.choices[0].message["content"]
        except Exception:
            pass

    # Profiling report saved
    try:
        profile = ProfileReport(df, minimal=True, explorative=True)
        path = tempfile.NamedTemporaryFile(delete=False, suffix=".html").name
        profile.to_file(path)
        profiling = path
    except Exception as e:
        profiling = None

    return {
        "category": category,
        "overview": overview,
        "narrative": narrative,
        "profiling": profiling,
        "tags": ["overview","top_performer","trend","highlight","narrative","recommendation"]
    }
