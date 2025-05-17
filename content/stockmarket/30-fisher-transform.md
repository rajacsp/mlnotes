---
title: 30-Fisher-Transform
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
import numpy as np
import matplotlib.pyplot as plt

# Step 1: Download historical data
symbol = "^GSPC"  # S&P 500 as an example
start = "2020-01-01"
end = "2023-12-31"
data = yf.download(symbol, start=start, end=end)

# Step 2: Calculate Fisher Transform
def calculate_fisher(data, period=10):
    # Ensure Lowest Low and Highest High are single-column Series
    data['Lowest Low'] = data['Low'].rolling(window=period, min_periods=1).min()
    data['Highest High'] = data['High'].rolling(window=period, min_periods=1).max()
    
    # Calculate normalized price (x) as a single-column Series
    data['x'] = 2 * ((data['Close'] - data['Lowest Low']) / 
                     (data['Highest High'] - data['Lowest Low']) - 0.5)
    
    # Clip x to stay within the range [-0.999, 0.999]
    data['x'] = data['x'].clip(lower=-0.999, upper=0.999)
    
    # Apply Fisher Transform
    data['Fisher'] = 0.5 * np.log((1 + data['x']) / (1 - data['x']))
    data['Fisher Signal'] = data['Fisher'].shift(1)  # Signal line
    
    return data

# Apply Fisher Transform calculation
period = 10
data = calculate_fisher(data, period)

# Step 3: Plot Close Price and Fisher Transform
plt.figure(figsize=(14, 7))

# Plot Close Price
plt.subplot(2, 1, 1)
plt.plot(data['Close'], label='Close Price', color='blue')
plt.title(f'{symbol} Close Price')
plt.xlabel('Date')
plt.ylabel('Price')
plt.legend()
plt.grid(True)

# Plot Fisher Transform
plt.subplot(2, 1, 2)
plt.plot(data['Fisher'], label='Fisher Transform', color='purple', linewidth=1.5)
plt.plot(data['Fisher Signal'], label='Fisher Signal', color='orange', linestyle='--', linewidth=1.5)
plt.axhline(0, color='black', linestyle='--', linewidth=1, label='Zero Line')
plt.title(f'Fisher Transform for {symbol}')
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

    /tmp/ipykernel_1236625/3302577336.py in ?()
         29     return data
         30 
         31 # Apply Fisher Transform calculation
         32 period = 10
    ---> 33 data = calculate_fisher(data, period)
         34 
         35 # Step 3: Plot Close Price and Fisher Transform
         36 plt.figure(figsize=(14, 7))


    /tmp/ipykernel_1236625/3302577336.py in ?(data, period)
         15     data['Lowest Low'] = data['Low'].rolling(window=period, min_periods=1).min()
         16     data['Highest High'] = data['High'].rolling(window=period, min_periods=1).max()
         17 
         18     # Calculate normalized price (x) as a single-column Series
    ---> 19     data['x'] = 2 * ((data['Close'] - data['Lowest Low']) / 
         20                      (data['Highest High'] - data['Lowest Low']) - 0.5)
         21 
         22     # Clip x to stay within the range [-0.999, 0.999]


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


    ValueError: Cannot set a DataFrame with multiple columns to the single column x



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