import numpy as np
import pandas as pd
from statsmodels.sandbox.stats.runs import runstest_1samp

# Example financial market data: Daily price changes (could be any financial asset)
price_changes = np.array([0.1, -0.2, 0.05, -0.05, 0.1, -0.1, 0.2, -0.15, 0.05])

# Runs Test for Randomness
z_stat, p_value = runstest_1samp(price_changes, correction=False)
print(f"Runs Test Z-statistic: {z_stat}, p-value: {p_value}")

# Hurst Exponent Function
def hurst_exponent(time_series):
    """Returns the Hurst Exponent of the time series"""
    lags = range(2, 100)
    tau = [np.sqrt(np.std(np.subtract(time_series[lag:], time_series[:-lag]))) for lag in lags]
    poly = np.polyfit(np.log(lags), np.log(tau), 1)
    return poly[0]*2.0

# Calculate Hurst Exponent
hurst_exp = hurst_exponent(price_changes)
print(f"Hurst Exponent: {hurst_exp}")