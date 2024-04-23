import numpy as np
import pandas as pd
from statsmodels.sandbox.stats.runs import runstest_1samp

# Preprocess the data
# Example data string with European decimal notation
data_str = "5005.44; 5019.02; 5030.10"

# Step 1: Replace commas with periods to conform to Python's float format

# Step 2: Split the string into a list of prices
data_list = data_str.split("; ")

# Step 3: Convert the strings to floats
data_floats = [float(price) for price in data_list]

# Assuming the data represents prices, calculate daily price changes
price_changes = np.diff(data_floats)

# Runs Test for Randomness
z_stat, p_value = runstest_1samp(price_changes, correction=False)
print(f"Runs Test Z-statistic: {z_stat}, p-value: {p_value}")

# Hurst Exponent Function
def hurst_exponent(time_series):
    """Returns the Hurst Exponent of the time series"""
    lags = range(2, 100)
    tau = [np.sqrt(np.std(np.subtract(time_series[lag:], time_series[:-lag]))) for lag in lags]
    # Ensure tau values are positive before taking logs
    tau = [x if x > 0 else np.nan for x in tau]
    # Use np.log1p for a more numerically stable log calculation, subtracting 1 after to adjust for np.log1p's behavior
    poly = np.polyfit(np.log1p(np.array(lags) - 1), np.log1p(np.array(tau) - 1), 1)
    return poly[0]*2.0

# Calculate Hurst Exponent
hurst_exp = hurst_exponent(price_changes)
print(f"Hurst Exponent: {hurst_exp}")

# Interpretation of Hurst Exponent:
# hurst < 0.5 - mean reverting series
# hurst = 0.5 - random walk
# hurst > 0.5 - trending series