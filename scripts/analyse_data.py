import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import statsmodels.api as sm
from pandas.plotting import register_matplotlib_converters

# Register converters to avoid warning
register_matplotlib_converters()

# Custom function to parse quantity (handling mixed types)
def parse_fail_quantity(value):
    try:
        return int(value)
    except ValueError:
        return pd.NA  # or np.nan or any other appropriate value for missing/invalid data

# Load the data
vw_stock = pd.read_csv('../data/volkswagen_stock_prices.csv', parse_dates=['Date'], index_col='Date')
sp500 = pd.read_csv('../data/sp500_index.csv', parse_dates=['Date'], index_col='Date')
try:
    # Read CSV file, handle mixed types in columns, and parse dates
    ftd_data = pd.read_csv('../data/ftd_data.csv',
                            dtype={'QUANTITY (FAILS)': 'str'},  # Specify dtype for columns with mixed types
                            parse_dates=['SETTLEMENT DATE'],
                            index_col='SETTLEMENT DATE',
                            converters={'QUANTITY (FAILS)': parse_fail_quantity})  # Custom converter for quantity

    # Filter out non-date rows from SETTLEMENT DATE
    ftd_data = ftd_data[pd.to_datetime(ftd_data.index, errors='coerce').notnull()]

    # Convert index to datetime and localize to UTC
    ftd_data.index = pd.to_datetime(ftd_data.index)
    ftd_data.index = ftd_data.index.tz_localize('UTC')
except pd.errors.ParserError as e:
    print(f"Error parsing CSV file: {e}")
    # Optionally, log or handle the error here
    ftd_data = None  # Assigning None or handling for the case where reading fails

# Display the DataFrame if successfully read
if ftd_data is not None:
    print(ftd_data.head())
else:
    print("Failed to read the CSV file.")

# Plot Volkswagen stock prices and FTD volumes if ftd_data is not None
if ftd_data is not None:
    fig, ax1 = plt.subplots()

    ax1.set_xlabel('Date')
    ax1.set_ylabel('Volkswagen Stock Price', color='tab:blue')
    ax1.plot(vw_stock.index, vw_stock['Close'], color='tab:blue')

    ax2 = ax1.twinx()
    ax2.set_ylabel('FTD Volume', color='tab:red')
    ax2.plot(ftd_data.index, ftd_data['QUANTITY (FAILS)'], color='tab:red')

    fig.tight_layout()
    plt.show()

    # Correlation analysis
    combined_data = vw_stock.join(ftd_data, how='inner')
    print(combined_data.corr())

    # Regression analysis
    X = combined_data['QUANTITY (FAILS)']
    y = combined_data['Close']
    X = sm.add_constant(X)  # Add an intercept to the model

    model = sm.OLS(y, X).fit()
    print(model.summary())
else:
    print("Skipping plotting and analysis due to missing FTD data.")
