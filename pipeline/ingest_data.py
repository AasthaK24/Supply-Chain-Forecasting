import pandas as pd

RAW_PATH = "../data/raw/train.csv"

def ingest_data(file_path: str = RAW_PATH) -> pd.DataFrame:
    """Load raw supply chain CSV data"""
    df = pd.read_csv(file_path, parse_dates=["date"])
    return df

if __name__ == "__main__":
    df = ingest_data()
    print("✅ Data Ingested. Shape:", df.shape)
    print(df.head())
