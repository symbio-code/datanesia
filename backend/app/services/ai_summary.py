import pandas as pd
import tempfile, os
from ydata_profiling import ProfileReport
from pandasai import SmartDataframe
from pandasai.llm.local_llm import LocalLLM
from app.core.detector import detect_dataset_category
from app.core.utils import parse_csv_bytes
import json
import openai
from app.core.config import AI_API_KEY

def generate_summary_from_lux(file_content: bytes, category: str = None):
    df = parse_csv_bytes(file_content)

    if not category:
        category = detect_dataset_category(df)

    overview = {
        "rows": len(df),
        "columns": len(df.columns),
    }

    prompts = {
        "sales": "You are a sales analyst. Write a summary in English and Bahasa Indonesia.",
        "marketing": "You are a marketing analyst. Write a summary in English and Bahasa Indonesia.",
        "finance": "You are a finance analyst. Write a summary in English and Bahasa Indonesia.",
        "saas": "You are a SaaS analyst. Write a summary in English and Bahasa Indonesia.",
        "general": "You are a data analyst. Provide key trends and highlights."
    }

    selected_prompt = prompts.get(category, prompts["general"])

    # 🧠 Local LLM first
    try:
        llm = LocalLLM()
        smart_df = SmartDataframe(df, config={"llm": llm})
        narrative = smart_df.chat(selected_prompt)
    except Exception as e:
        narrative = f"Local LLM unavailable ({e})"

    # 🌍 Fallback to OpenAI API
    if openai and AI_API_KEY:
        try:
            openai.api_key = AI_API_KEY
            res = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "user", "content": f"{selected_prompt}\n\nDataframe columns: {', '.join(df.columns)}"}
                ],
                temperature=0.7,
            )
            narrative = res.choices[0].message["content"]
        except Exception:
            pass

    # Optional profiling
    try:
        profile = ProfileReport(df, minimal=True, explorative=True)
        path = tempfile.NamedTemporaryFile(delete=False, suffix=".html").name
        profile.to_file(path)
        profiling = path
    except Exception:
        profiling = None

    return {
        "category": category,
        "overview": overview,
        "narrative": narrative,
        "profiling": profiling,
        "tags": ["overview", "top_performer", "trend", "highlight", "narrative", "recommendation"]
    }
