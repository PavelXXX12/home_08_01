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

periods = {
    "monthly-sales-of-company-x-jan-6.csv": 12,
    "monthly-boston-armed-robberies-j.csv": 12,
    "international-airline-passengers.csv": 12,
    "mean-monthly-air-temperature-deg.csv": 12,
    "weekly-closings-of-the-dowjones-.csv": 52,
    "daily-total-female-births-in-cal.csv": 365
}

from statsmodels.tsa.stattools import adfuller


def test_stationarity(series):
    result = adfuller(series.dropna())
    adf_statistic = result[0]
    p_value = result[1]
    critical_values = result[4]
    if p_value < 0.05:
        print("Ряд стационарен ")
    else:
        print("Ряд не стационарен")
    return {
        "ADF Statistic": adf_statistic,
        "p-value": p_value,
        "Critical Values": critical_values
    }


for name, path in files.items():
    series = pd.read_csv(path, header=0, index_col=0, parse_dates=True, date_format="%Y-%m")
    print(f"\nРезультаты для {name}:")
    test_stationarity(series)
def log_transform(series):
    return np.log(series)
def difference(series):
    return series.diff()
for name, path in files.items():
    series = pd.read_csv(path, header=0, index_col=0, parse_dates=True, date_format="%Y-%m")
    log_series = log_transform(series)
    diff_series = difference(log_series)
    result = adfuller(diff_series.dropna())
    adf_statistic = result[0]
    p_value = result[1]
    critical_values = result[4]
for name, path in files.items():
    series = pd.read_csv(path, header=0, index_col=0, parse_dates=True, date_format="%Y-%m")
    print(f"\nРезультаты 2 для {name}:")
    file_key = list(files.keys())[2]
    file_path = files[file_key]
    if p_value < 0.05:
        print("Ряд стационарен ")
    else:
        print("Ряд не стационарен ")
    # log_series = log_transform(series)
    # diff_series = difference(log_series)
    # log_series = log_transform(series)
    # diff_series = difference(log_series)
    # if p_value < 0.05:
    #     print("Ряд стационарен.")
    # else:
    #     print("Ряд не стационарен .")
