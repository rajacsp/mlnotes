---
title: 12-Supertrend-Indicator
date: 2025-05-17
author: Your Name
cell_count: 10
score: 10
---

```python
# Created: 20250103
```


```python
import pyutil as pyu
pyu.get_local_pyinfo()
```




    'conda env: ml312-2024; pyv: 3.12.7 | packaged by Anaconda, Inc. | (main, Oct  4 2024, 13:27:36) [GCC 11.2.0]'




```python
print(pyu.ps2("requests"))
```

    requests==2.32.3
    



```python
import yfinance as yf
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
```


```python
import yfinance as yf
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Step 1: Download historical data
symbol = "^GSPC"  # S&P 500 as an example
start = "2020-01-01"
end = "2023-12-31"
data = yf.download(symbol, start=start, end=end)

# Step 2: Calculate ATR
def calculate_atr(data, atr_window=10):
    data['High-Low'] = data['High'] - data['Low']
    data['High-Close'] = abs(data['High'] - data['Close'].shift(1))
    data['Low-Close'] = abs(data['Low'] - data['Close'].shift(1))
    data['True Range'] = data[['High-Low', 'High-Close', 'Low-Close']].max(axis=1)
    data['ATR'] = data['True Range'].rolling(window=atr_window).mean()
    return data

# Step 3: Calculate Supertrend
def calculate_supertrend(data, multiplier=3, atr_window=10):
    data = calculate_atr(data, atr_window)
    
    # Calculate Basic Upper and Lower Bands
    upper_band = ((data['High'] + data['Low']) / 2) + (multiplier * data['ATR'])
    lower_band = ((data['High'] + data['Low']) / 2) - (multiplier * data['ATR'])
    
    # Assign calculated Series to the DataFrame
    data['Basic Upper Band'] = upper_band
    data['Basic Lower Band'] = lower_band
    
    data['Supertrend'] = np.nan
    in_uptrend = True  # Initial trend is uptrend

    for i in range(1, len(data)):
        if in_uptrend:
            if data['Close'].iloc[i] < data['Basic Upper Band'].iloc[i]:
                in_uptrend = False
            data.loc[data.index[i], 'Supertrend'] = max(
                data['Basic Lower Band'].iloc[i], 
                data['Supertrend'].iloc[i - 1]
            )
        else:
            if data['Close'].iloc[i] > data['Basic Lower Band'].iloc[i]:
                in_uptrend = True
            data.loc[data.index[i], 'Supertrend'] = min(
                data['Basic Upper Band'].iloc[i], 
                data['Supertrend'].iloc[i - 1]
            )

    return data

# Apply the Supertrend calculation
data = calculate_supertrend(data)

# Step 4: Plot Supertrend
plt.figure(figsize=(14, 7))
plt.plot(data['Close'], label='Close Price', color='blue')
plt.plot(data['Supertrend'], label='Supertrend', color='red', linestyle='--')
plt.fill_between(data.index, data['Supertrend'], data['Close'], 
                 where=data['Close'] >= data['Supertrend'], 
                 color='green', alpha=0.3, label='Uptrend')
plt.fill_between(data.index, data['Supertrend'], data['Close'], 
                 where=data['Close'] < data['Supertrend'], 
                 color='red', alpha=0.3, label='Downtrend')
plt.title(f'Supertrend Indicator for {symbol}')
plt.xlabel('Date')
plt.ylabel('Price')
plt.legend(loc='best')
plt.grid(True)
plt.show()
```

    [*********************100%***********************]  1 of 1 completed



    ---------------------------------------------------------------------------

    ValueError                                Traceback (most recent call last)

    /tmp/ipykernel_947826/1063826374.py in ?()
         51 
         52     return data
         53 
         54 # Apply the Supertrend calculation
    ---> 55 data = calculate_supertrend(data)
         56 
         57 # Step 4: Plot Supertrend
         58 plt.figure(figsize=(14, 7))


    /tmp/ipykernel_947826/1063826374.py in ?(data, multiplier, atr_window)
         26     upper_band = ((data['High'] + data['Low']) / 2) + (multiplier * data['ATR'])
         27     lower_band = ((data['High'] + data['Low']) / 2) - (multiplier * data['ATR'])
         28 
         29     # Assign calculated Series to the DataFrame
    ---> 30     data['Basic Upper Band'] = upper_band
         31     data['Basic Lower Band'] = lower_band
         32 
         33     data['Supertrend'] = np.nan


    ~/miniconda3/envs/ml312-2024/lib/python3.12/site-packages/pandas/core/frame.py in ?(self, key, value)
       4297             self._setitem_frame(key, value)
       4298         elif isinstance(key, (Series, np.ndarray, list, Index)):
       4299             self._setitem_array(key, value)
       4300         elif isinstance(value, DataFrame):
    -> 4301             self._set_item_frame_value(key, value)
       4302         elif (
       4303             is_list_like(value)
       4304             and not self.columns.is_unique


    ~/miniconda3/envs/ml312-2024/lib/python3.12/site-packages/pandas/core/frame.py in ?(self, key, value)
       4455 
       4456             return self.isetitem(locs, value)
       4457 
       4458         if len(value.columns) > 1:
    -> 4459             raise ValueError(
       4460                 "Cannot set a DataFrame with multiple columns to the single "
       4461                 f"column {key}"
       4462             )


    ValueError: Cannot set a DataFrame with multiple columns to the single column Basic Upper Band



```python
# Step 2: Calculate ATR
def calculate_atr(data, atr_window=10):
    data['High-Low'] = data['High'] - data['Low']
    data['High-Close'] = abs(data['High'] - data['Close'].shift(1))
    data['Low-Close'] = abs(data['Low'] - data['Close'].shift(1))
    data['True Range'] = data[['High-Low', 'High-Close', 'Low-Close']].max(axis=1)
    data['ATR'] = data['True Range'].rolling(window=atr_window).mean()
    return data

# Step 3: Calculate Supertrend
def calculate_supertrend(data, multiplier=3, atr_window=10):
    data = calculate_atr(data, atr_window)
    # Ensure correct column assignment with a single series
    data['Basic Upper Band'] = ((data['High'] + data['Low']) / 2) + (multiplier * data['ATR'])
    data['Basic Lower Band'] = ((data['High'] + data['Low']) / 2) - (multiplier * data['ATR'])
    
    data['Supertrend'] = np.nan
    in_uptrend = True  # Initial trend is uptrend

    for i in range(len(data)):
        if i == 0:
            data.loc[data.index[i], 'Supertrend'] = data.loc[data.index[i], 'Basic Lower Band']
            continue

        if in_uptrend:
            if data.loc[data.index[i], 'Close'] < data.loc[data.index[i], 'Basic Upper Band']:
                in_uptrend = False
            data.loc[data.index[i], 'Supertrend'] = max(
                data.loc[data.index[i], 'Basic Lower Band'], 
                data.loc[data.index[i - 1], 'Supertrend']
            )
        else:
            if data.loc[data.index[i], 'Close'] > data.loc[data.index[i], 'Basic Lower Band']:
                in_uptrend = True
            data.loc[data.index[i], 'Supertrend'] = min(
                data.loc[data.index[i], 'Basic Upper Band'], 
                data.loc[data.index[i - 1], 'Supertrend']
            )

    return data
```


```python

```


```python
def show_graph(symbol):

    # Step 1: Download historical data
    start = "2020-01-01"
    end = "2023-12-31"
    data = yf.download(symbol, start=start, end=end)
    
    # Apply the Supertrend calculation
    data = calculate_supertrend(data)
    
    # Step 4: Plot Supertrend
    plt.figure(figsize=(14, 7))
    plt.plot(data['Close'], label='Close Price', color='blue')
    plt.plot(data['Supertrend'], label='Supertrend', color='red', linestyle='--')
    plt.fill_between(data.index, data['Supertrend'], data['Close'], 
                     where=data['Close'] >= data['Supertrend'], 
                     color='green', alpha=0.3, label='Uptrend')
    plt.fill_between(data.index, data['Supertrend'], data['Close'], 
                     where=data['Close'] < data['Supertrend'], 
                     color='red', alpha=0.3, label='Downtrend')
    plt.title(f'Supertrend Indicator for {symbol}')
    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.legend(loc='best')
    plt.grid(True)
    plt.show()
```


```python
show_graph("AMZN")
```

    [*********************100%***********************]  1 of 1 completed



    ---------------------------------------------------------------------------

    ValueError                                Traceback (most recent call last)

    /tmp/ipykernel_947826/73109923.py in ?()
    ----> 1 show_graph("AMZN")
    

    /tmp/ipykernel_947826/2804851505.py in ?(symbol)
          5     end = "2023-12-31"
          6     data = yf.download(symbol, start=start, end=end)
          7 
          8     # Apply the Supertrend calculation
    ----> 9     data = calculate_supertrend(data)
         10 
         11     # Step 4: Plot Supertrend
         12     plt.figure(figsize=(14, 7))


    /tmp/ipykernel_947826/4282768184.py in ?(data, multiplier, atr_window)
         11 def calculate_supertrend(data, multiplier=3, atr_window=10):
         12     data = calculate_atr(data, atr_window)
         13     # Ensure correct column assignment with a single series
    ---> 14     data['Basic Upper Band'] = ((data['High'] + data['Low']) / 2) + (multiplier * data['ATR'])
         15     data['Basic Lower Band'] = ((data['High'] + data['Low']) / 2) - (multiplier * data['ATR'])
         16 
         17     data['Supertrend'] = np.nan


    ~/miniconda3/envs/ml312-2024/lib/python3.12/site-packages/pandas/core/frame.py in ?(self, key, value)
       4297             self._setitem_frame(key, value)
       4298         elif isinstance(key, (Series, np.ndarray, list, Index)):
       4299             self._setitem_array(key, value)
       4300         elif isinstance(value, DataFrame):
    -> 4301             self._set_item_frame_value(key, value)
       4302         elif (
       4303             is_list_like(value)
       4304             and not self.columns.is_unique


    ~/miniconda3/envs/ml312-2024/lib/python3.12/site-packages/pandas/core/frame.py in ?(self, key, value)
       4455 
       4456             return self.isetitem(locs, value)
       4457 
       4458         if len(value.columns) > 1:
    -> 4459             raise ValueError(
       4460                 "Cannot set a DataFrame with multiple columns to the single "
       4461                 f"column {key}"
       4462             )


    ValueError: Cannot set a DataFrame with multiple columns to the single column Basic Upper Band



```python

```


---
**Score: 10**