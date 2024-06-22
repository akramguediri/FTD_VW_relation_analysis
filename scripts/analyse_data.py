import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import statsmodels.api as sm

# Load the data
vw_stock = pd.read_csv('data/volkswagen_stock_prices.csv', parse_dates=['Date'], index_col='Date')
ftd_data = pd.read_csv('data/ftd_data.csv', parse_dates=['Date'], index_col='Date')
sp500 = pd.read_csv('data/sp500_index.csv', parse_dates=['Date'], index_col='Date')

# Plot Volkswagen stock prices and FTD volumes
fig, ax1 = plt.subplots()

ax1.set_xlabel('Date')
ax1.set_ylabel('Volkswagen Stock Price', color='tab:blue')
ax1.plot(vw_stock.index, vw_stock['Close'], color='tab:blue')

ax2 = ax1.twinx()
ax2.set_ylabel('FTD Volume', color='tab:red')
ax2.plot(ftd_data.index, ftd_data['FTD_Volume'], color='tab:red')

fig.tight_layout()
plt.show()

# Correlation analysis
combined_data = vw_stock.join(ftd_data, how='inner')
print(combined_data.corr())

# Regression analysis
X = combined_data['FTD_Volume']
y = combined_data['Close']
X = sm.add_constant(X) # Add an intercept to the model

model = sm.OLS(y, X).fit()
print(model.summary())
