# 📦 Supply Chain Demand Forecasting

## 📌 Project Overview  
This project demonstrates an **end-to-end supply chain demand forecasting system**.  
It combines:  
- **Python + Prophet** for time-series forecasting,  
- an automated **data pipeline**, and  
- a **Power BI dashboard** for business insights.  

The goal is to forecast future product demand to help supply chain teams optimize **procurement, inventory, and logistics decisions**.  

---

## ⚙️ Tech Stack  
- **Python** (Pandas, Prophet, Matplotlib)  
- **Power BI** (Dashboarding & business reporting)  
- **GitHub** (Version control)  
- **Excel/CSV** (Data input/output)  

---
## Data Pipeline

- **ingest_data.py** → loads raw data (train.csv).

- **process_data.py** → aggregates sales by date, store, item.

- **forecast.py** → trains Prophet and generates 90-day forecasts.

- **run_pipeline.py** → orchestrates all steps → saves forecast.csv.

# Run the pipeline with:
```bash
cd pipeline
python run_pipeline.py
```
## 📂 Project Structure  
```bash
supply-chain-forecasting/
│── data/
│   ├── raw/ (train.csv)
│   ├── processed/ (processed_data.csv, forecast.csv)
│── notebooks/
│   ├── eda.ipynb
│   ├── forecasting.ipynb
│── pipeline/
│   ├── ingest_data.py
│   ├── process_data.py
│   ├── forecast.py
│   ├── run_pipeline.py
│── dashboard/
│   ├── supply_forecast.pbix
│   ├── screenshots/
│── README.md
```
## Power BI Dashboard
The dashboard provides business-friendly insights:

🔹 KPIs

- Total Forecasted Sales (Next 90 Days)

- % Growth vs Last 90 Days

🔹 Visuals

- Actual vs Forecast with confidence intervals

- Weekly & Yearly seasonality patterns

- Long-term trend component

![Dashboard Preview](dashboard/image.png)

## Business Value

- This system helps supply chain teams optimize inventory by forecasting demand:

- Prevents stockouts and overstocking.

- Enables data-driven procurement planning.

- Provides confidence intervals for risk-aware decision making.
