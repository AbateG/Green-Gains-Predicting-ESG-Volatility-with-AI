import pandas as pd
import yfinance as yf
import wbgapi as wb
import os

# Set up directories
os.makedirs('data/csv_originals', exist_ok=True)
os.makedirs('data/excel_copies', exist_ok=True)

# 1. ESG Data: Use sample data (in real scenario, download from public sources like MSCI or Yahoo)
esg_sample = pd.DataFrame({
    'company': ['Apple', 'Tesla', 'ExxonMobil'],
    'esg_score': [85, 78, 45],
    'sector': ['Technology', 'Automotive', 'Energy']
})
esg_sample.to_csv('data/csv_originals/esg_data.csv', index=False)

# 2. Download Stock Data using yfinance
tickers = ['AAPL', 'TSLA', 'XOM']  # Corresponding tickers
stock_data = yf.download(tickers, start='2020-01-01', end='2024-01-01')
stock_data.to_csv('data/csv_originals/stock_prices.csv')

# 3. Download Economic Data from World Bank
try:
    # Inflation rate (annual %)
    inflation_df = wb.data.DataFrame('FP.CPI.TOTL.ZG', 'USA', time=range(2020, 2024))
    inflation_df.to_csv('data/csv_originals/inflation_usa.csv')
except Exception as e:
    print(f"Error downloading inflation data: {e}")

try:
    # Unemployment rate
    unemployment_df = wb.data.DataFrame('SL.UEM.TOTL.ZS', 'USA', time=range(2020, 2024))
    unemployment_df.to_csv('data/csv_originals/unemployment_usa.csv')
except Exception as e:
    print(f"Error downloading unemployment data: {e}")

print("Data prepared and saved to data/csv_originals/")
