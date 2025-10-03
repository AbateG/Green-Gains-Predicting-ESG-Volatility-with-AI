import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error
import matplotlib.pyplot as plt
import numpy as np

# Load data
esg = pd.read_csv('data/csv_originals/esg_data.csv')
stocks = pd.read_csv('data/csv_originals/stock_prices.csv', header=[0,1], index_col=0)
inflation = pd.read_csv('data/csv_originals/inflation_usa.csv')
unemployment = pd.read_csv('data/csv_originals/unemployment_usa.csv')

# Process stocks: Calculate volatility (annualized std of returns)
stocks.index = pd.to_datetime(stocks.index)
returns = stocks.pct_change().dropna()
volatility = returns.std() * (252**0.5)  # Annualized volatility

# Map to ESG companies
tickers = ['AAPL', 'TSLA', 'XOM']
esg_vol = pd.DataFrame({
    'company': ['Apple', 'Tesla', 'ExxonMobil'],
    'ticker': tickers,
    'esg_score': [85, 78, 45],
    'volatility': [volatility.xs('Close', level=0)[t] for t in tickers]
})

# Add economic factors (average values)
avg_inflation = inflation.iloc[0, 1:].mean()  # Skip country column
avg_unemployment = unemployment.iloc[0, 1:].mean()
esg_vol['inflation'] = avg_inflation
esg_vol['unemployment'] = avg_unemployment

# ML Model: Predict volatility based on ESG and economic factors
X = esg_vol[['esg_score', 'inflation', 'unemployment']]
y = esg_vol['volatility']

# Since small dataset, use all for training/demo
model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X, y)
predictions = model.predict(X)
rmse = mean_squared_error(y, predictions, squared=False)
print(f'RMSE: {rmse}')

# Visualization
plt.scatter(y, predictions)
plt.xlabel('Actual Volatility')
plt.ylabel('Predicted Volatility')
plt.title('Volatility Prediction (Demo)')
plt.savefig('data/excel_copies/volatility_prediction.png')
plt.show()

# Export summary
esg_vol.to_csv('data/excel_copies/analysis_summary.csv', index=False)
print("Analysis complete. Summary saved.")
