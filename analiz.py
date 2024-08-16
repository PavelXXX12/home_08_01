import matplotlib.pyplot as plt
from statsmodels.tsa.seasonal import seasonal_decompose
from statsmodels.tsa.stattools import adfuller
import pandas as pd
from statsmodels.tsa.stattools import adfuller
import numpy as np


files = {
    "monthly-sales-of-company-x-jan-6.csv": "monthly-sales-of-company-x-jan-6.csv",
    "monthly-boston-armed-robberies-j.csv": "monthly-boston-armed-robberies-j.csv",
    "international-airline-passengers.csv": "international-airline-passengers.csv",
    "mean-monthly-air-temperature-deg.csv": "mean-monthly-air-temperature-deg.csv",
    "weekly-closings-of-the-dowjones-.csv": "weekly-closings-of-the-dowjones-.csv",
    "daily-total-female-births-in-cal.csv": "daily-total-female-births-in-cal.csv"
}

file_path = 'monthly-sales-of-company-x-jan-6.csv'
data = pd.read_csv(file_path, header=0, index_col=0, parse_dates=True)

def analyze_time_series(data, title="Time Series Analysis", filename="data"):
    title = f"Time Series Analysis - {filename}"
    decomposition = seasonal_decompose(data, model='additive', period=12)
    plt.figure(figsize=(12, 10))
    plt.suptitle(title, y=1.02)
    plt.subplot(411)
    plt.plot(data, label='Original Data')
    plt.legend(loc='best')
    plt.subplot(412)
    plt.plot(decomposition.trend, label='Trend')
    plt.legend(loc='best')
    plt.subplot(413)
    plt.plot(decomposition.seasonal, label='Seasonal')
    plt.legend(loc='best')
    plt.subplot(414)
    plt.plot(decomposition.resid, label='Residual')
    plt.legend(loc='best')
    plt.tight_layout()
    plt.suptitle(title, y=1.02)
    plt.tight_layout(rect=[0, 0, 1, 0.96])
    plt.show()

    # Тест Дики-Фуллера
    result = adfuller(data.dropna())
    p_value = result[1]

    if p_value < 0.05:
        stationarity = f"Ряд стационарен  Файл: {filename}"
    else:
        stationarity = f"Ряд не стационарен  Файл: {filename}"

    print(stationarity)
    return {
        "Stationarity Conclusion": stationarity
    }

for name, path in files.items():
    series = pd.read_csv(path, header=0, index_col=0, parse_dates=True, date_format="%Y-%m")
    result = analyze_time_series(series, filename=name)


