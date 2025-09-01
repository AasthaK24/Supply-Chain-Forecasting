import ingest_data
import process_data
import forecast
import pandas as pd

RAW_PATH = "../data/raw/train.csv"
PROCESSED_PATH = "../data/processed/processed_data.csv"
FORECAST_PATH = "../data/processed/forecast.csv"

if __name__ == "__main__":
    print("🔹 Step 1: Ingesting Data...")
    df_raw = ingest_data.ingest_data(RAW_PATH)

    print("🔹 Step 2: Processing Data...")
    df_processed = process_data.process_data(df_raw)
    df_processed.to_csv(PROCESSED_PATH, index=False)

    print("🔹 Step 3: Forecasting...")
    df_forecast = forecast.run_forecast(df_processed)
    df_forecast.to_csv(FORECAST_PATH, index=False)

    print("✅ Pipeline completed. Forecast saved to:", FORECAST_PATH)
