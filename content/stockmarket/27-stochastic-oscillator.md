---
title: 27-Stochastic-Oscillator
date: 2025-01-04
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

# Step 2: Calculate Stochastic Oscillator
def calculate_stochastic(data, k_period=14, d_period=3):
    # Calculate Lowest Low and Highest High as single-column Series
    data['Lowest Low'] = data['Low'].rolling(window=k_period).min()
    data['Highest High'] = data['High'].rolling(window=k_period).max()
    
    # Calculate %K
    data['%K'] = ((data['Close'] - data['Lowest Low']) / 
                  (data['Highest High'] - data['Lowest Low'])) * 100
    
    # Calculate %D (smoothed %K)
    data['%D'] = data['%K'].rolling(window=d_period).mean()
    
    return data

# Apply Stochastic Oscillator calculation
k_period = 14  # Default period for %K
d_period = 3   # Smoothing period for %D
data = calculate_stochastic(data, k_period, d_period)

# Step 3: Plot Close Price and Stochastic Oscillator
plt.figure(figsize=(14, 7))

# Plot Close Price
plt.subplot(2, 1, 1)
plt.plot(data['Close'], label='Close Price', color='blue')
plt.title(f'{symbol} Close Price')
plt.xlabel('Date')
plt.ylabel('Price')
plt.legend()
plt.grid(True)

# Plot Stochastic Oscillator
plt.subplot(2, 1, 2)
plt.plot(data['%K'], label='%K (Stochastic)', color='green', linewidth=1.5)
plt.plot(data['%D'], label='%D (Smoothed)', color='red', linewidth=1.5)
plt.axhline(80, color='black', linestyle='--', linewidth=1, label='Overbought (80)')
plt.axhline(20, color='black', linestyle='--', linewidth=1, label='Oversold (20)')
plt.title(f'Stochastic Oscillator for {symbol}')
plt.xlabel('Date')
plt.ylabel('Value')
plt.legend(loc='best')
plt.grid(True)

plt.tight_layout()
plt.show()
```

    [*********************100%***********************]  1 of 1 completed



    ---------------------------------------------------------------------------

    ValueError                                Traceback (most recent call last)

    /tmp/ipykernel_1087535/2340797514.py in ?()
         25 
         26 # Apply Stochastic Oscillator calculation
         27 k_period = 14  # Default period for %K
         28 d_period = 3   # Smoothing period for %D
    ---> 29 data = calculate_stochastic(data, k_period, d_period)
         30 
         31 # Step 3: Plot Close Price and Stochastic Oscillator
         32 plt.figure(figsize=(14, 7))


    /tmp/ipykernel_1087535/2340797514.py in ?(data, k_period, d_period)
         14     data['Lowest Low'] = data['Low'].rolling(window=k_period).min()
         15     data['Highest High'] = data['High'].rolling(window=k_period).max()
         16 
         17     # Calculate %K
    ---> 18     data['%K'] = ((data['Close'] - data['Lowest Low']) / 
         19                   (data['Highest High'] - data['Lowest Low'])) * 100
         20 
         21     # Calculate %D (smoothed %K)


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


    ValueError: Cannot set a DataFrame with multiple columns to the single column %K



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