---
title: Arima-2
date: 2024-12-26
author: Your Name
cell_count: 3
score: 0
---

   https://machinelearningmastery.com/autoregression-models-time-series-forecasting-python/
   https://datamarket.com/data/set/2324/daily-minimum-temperatures-in-melbourne-australia-1981-1990#!ds=2324&display=line
   https://stackoverflow.com/questions/31494870/pandas-dataframe-no-numeric-data-to-plot-error
   https://en.wikipedia.org/wiki/Pearson_correlation_coefficient 

```python
import pandas as pd
from matplotlib import pyplot as plt
from pandas.plotting import lag_plot

# Load the dataset using pandas.read_csv
series = pd.read_csv(
    'daily-minimum-temperatures.csv',
    header=0,
    index_col=0,
    parse_dates=True
)

# Convert the data to numeric if necessary
series = series.squeeze().astype(float)  # Ensure it's a Series

# Uncomment to view data or plot the time series
# print(series.head())
# series.plot()
# plt.title("Daily Minimum Temperatures")
# plt.show()

# Lag plot
lag_plot(series)
plt.title("Lag Plot of Daily Minimum Temperatures")
plt.show()
```


    
![png](/mlnotes/images/arima-2_1_0.png)
    



```python

```


---
**Score: 0**