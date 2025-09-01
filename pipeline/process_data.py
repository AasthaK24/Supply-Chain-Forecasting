import pandas as pd

def process_data(df: pd.DataFrame) -> pd.DataFrame:
    """Aggregate data by date, store, and item"""
    df_agg = df.groupby(["date", "store", "item"])["sales"].sum().reset_index()
    return df_agg

if __name__ == "__main__":
    raw = pd.read_csv("../data/raw/train.csv", parse_dates=["date"])
    processed = process_data(raw)
    processed.to_csv("../data/processed/processed_data.csv", index=False)
    print("✅ Data Processed. Shape:", processed.shape)
    print(processed.head())
