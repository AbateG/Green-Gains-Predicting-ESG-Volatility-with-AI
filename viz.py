import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load processed data
esg = pd.read_csv('data/csv_originals/esg_data.csv')
stocks = pd.read_csv('data/csv_originals/stock_prices.csv', header=[0,1], index_col=0)
inflation = pd.read_csv('data/csv_originals/inflation_usa.csv')
unemployment = pd.read_csv('data/csv_originals/unemployment_usa.csv')

# Simple viz: ESG scores
plt.figure(figsize=(8,5))
sns.barplot(data=esg, x='company', y='esg_score')
plt.title('ESG Scores by Company')
plt.savefig('data/excel_copies/esg_scores.png')
plt.show()

# Stock prices over time (simplified)
stocks.index = pd.to_datetime(stocks.index)
stocks.xs('Close', axis=1, level=0).plot(figsize=(10,6))
plt.title('Stock Prices Over Time')
plt.savefig('data/excel_copies/stock_prices.png')
plt.show()

# Economic indicators
years = inflation.columns[1:]  # YR2020 etc.
plt.figure(figsize=(8,5))
plt.plot(years, inflation.iloc[0, 1:], label='Inflation')
plt.plot(years, unemployment.iloc[0, 1:], label='Unemployment')
plt.legend()
plt.title('Economic Indicators')
plt.savefig('data/excel_copies/economic_indicators.png')
plt.show()

print("Visualizations saved to data/excel_copies/")
