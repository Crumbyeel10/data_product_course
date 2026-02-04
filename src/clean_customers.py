import pandas as pd

def clean_customers(df: pd.DataFrame) -> pd.DataFrame:
    out = df.copy()
    out["name"] = out["name"].astype(str).str.strip()
    out["email"] = out["email"].astype(str).str.strip().str.lower()
    out["created_at"] = pd.to_datetime(out["created_at"], errors="coerce")
    return out

def validate_customers(df: pd.DataFrame) -> None:
    if df["customer_id"].isna().sum() != 0:
        raise ValueError("customer_id nulos")
    if df.duplicated(subset=["customer_id"]).sum() != 0:
        raise ValueError("customer_id duplicados")
    if df["created_at"].isna().sum() != 0:
        raise ValueError("created_at inválidos")
