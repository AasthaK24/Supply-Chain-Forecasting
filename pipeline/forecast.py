import pandas as pd
from prophet import Prophet

def run_forecast(df: pd.DataFrame, periods: int = 90) -> pd.DataFrame:
    """Fit Prophet model and forecast demand"""
    # Prepare for Prophet
    df_prophet = df.groupby("date")["sales"].sum().reset_index()
    df_prophet.columns = ["ds", "y"]

    # Model
    model = Prophet(yearly_seasonality=True, weekly_seasonality=True)
    model.fit(df_prophet)

    # Future dates
    future = model.make_future_dataframe(periods=periods)
    forecast = model.predict(future)

    return forecast

if __name__ == "__main__":
    df = pd.read_csv("../data/processed/processed_data.csv", parse_dates=["date"])
    forecast = run_forecast(df)
    forecast.to_csv("../data/processed/forecast.csv", index=False)
    print("✅ Forecast Generated. Shape:", forecast.shape)
    print(forecast[["ds", "yhat", "yhat_lower", "yhat_upper"]].tail())
