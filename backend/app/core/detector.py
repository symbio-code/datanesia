def detect_dataset_category(df):
    col_names = [c.lower() for c in df.columns]
    if any(k in col_names for k in ["sales", "revenue", "product", "quantity", "order"]):
        return "sales"
    if any(k in col_names for k in ["campaign", "click", "impression", "conversion", "ctr", "roi"]):
        return "marketing"
    if any(k in col_names for k in ["expense", "profit", "income", "cost", "balance", "cashflow"]):
        return "finance"
    if any(k in col_names for k in ["user", "plan", "churn", "mrr", "subscription", "retention"]):
        return "saas"
    return "general"
