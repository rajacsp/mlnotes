---
title: 48-Volatality-Stop
date: 2025-05-17
author: Your Name
cell_count: 9
score: 5
---

```python
# Created: 20250104
```


```python
import pyutil as pyu
pyu.get_local_pyinfo()
```




    'conda env: ml312-2024; pyv: 3.12.7 | packaged by Anaconda, Inc. | (main, Oct  4 2024, 13:27:36) [GCC 11.2.0]'




```python
print(pyu.ps2("yfinance pandas matplotlib"))
```

    yfinance==0.2.51
    pandas==2.2.3
    matplotlib==3.9.3
    



```python
import yfinance as yf
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
```


```python
import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

# Step 1: Download historical data
symbol = "^GSPC"  # S&P 500 as an example
start = "2020-01-01"
end = "2023-12-31"
data = yf.download(symbol, start=start, end=end)

# Step 2: Calculate Volatility Stop
def calculate_volatility_stop(data, atr_period=14, multiplier=3):
    # True Range (TR)
    data['High-Low'] = data['High'] - data['Low']
    data['High-Close'] = abs(data['High'] - data['Close'].shift(1))
    data['Low-Close'] = abs(data['Low'] - data['Close'].shift(1))
    data['True Range'] = data[['High-Low', 'High-Close', 'Low-Close']].max(axis=1)
    
    # Average True Range (ATR)
    data['ATR'] = data['True Range'].rolling(window=atr_period).mean()
    
    # Determine trend direction
    data['Trend'] = (data['Close'] > data['Close'].shift(1)).astype(int)  # 1 for uptrend, 0 for downtrend
    
    # Calculate Volatility Stop
    data['Volatility Stop'] = data['Close'] - multiplier * data['ATR']
    data.loc[data['Trend'] == 0, 'Volatility Stop'] = data['Close'] + multiplier * data['ATR']
    
    return data

# Apply Volatility Stop calculation
data = calculate_volatility_stop(data)

# Step 3: Plot Close Price and Volatility Stop
plt.figure(figsize=(14, 7))

# Plot Close Price
plt.plot(data['Close'], label='Close Price', color='blue', linewidth=1)

# Plot Volatility Stop
plt.plot(data['Volatility Stop'], label='Volatility Stop', color='red', linestyle='--', linewidth=1.5)

# Customize the plot
plt.title(f'{symbol} Volatility Stop (ATR Period: 14, Multiplier: 3)')
plt.xlabel('Date')
plt.ylabel('Price')
plt.legend(loc='best')
plt.grid(True)
plt.tight_layout()
plt.show()
```

    [*********************100%***********************]  1 of 1 completed



    ---------------------------------------------------------------------------

    ValueError                                Traceback (most recent call last)

    /tmp/ipykernel_1338088/2777029421.py in ?()
         28 
         29     return data
         30 
         31 # Apply Volatility Stop calculation
    ---> 32 data = calculate_volatility_stop(data)
         33 
         34 # Step 3: Plot Close Price and Volatility Stop
         35 plt.figure(figsize=(14, 7))


    /tmp/ipykernel_1338088/2777029421.py in ?(data, atr_period, multiplier)
         22     # Determine trend direction
         23     data['Trend'] = (data['Close'] > data['Close'].shift(1)).astype(int)  # 1 for uptrend, 0 for downtrend
         24 
         25     # Calculate Volatility Stop
    ---> 26     data['Volatility Stop'] = data['Close'] - multiplier * data['ATR']
         27     data.loc[data['Trend'] == 0, 'Volatility Stop'] = data['Close'] + multiplier * data['ATR']
         28 
         29     return data


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


    ValueError: Cannot set a DataFrame with multiple columns to the single column Volatility Stop



```python

```


```python
def show_graph(symbol):

pass
```


```python
show_graph("AMZN")
```


    ---------------------------------------------------------------------------

    NameError                                 Traceback (most recent call last)

    Cell In[5], line 1
    ----> 1 show_graph("AMZN")


    NameError: name 'show_graph' is not defined



```python

```


---
**Score: 5**