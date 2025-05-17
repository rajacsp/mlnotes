---
title: 28-Vortex-Indicator
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

# Step 2: Calculate Vortex Indicator
def calculate_vortex(data, period=14):
    high = data['High']
    low = data['Low']
    close = data['Close']
    
    # Calculate True Range (TR)
    tr1 = high - low
    tr2 = abs(high - close.shift(1))
    tr3 = abs(low - close.shift(1))
    tr = pd.concat([tr1, tr2, tr3], axis=1).max(axis=1)  # Ensure TR is a Series
    
    # Calculate +VM and -VM
    plus_vm = abs(high - low.shift(1))
    minus_vm = abs(low - high.shift(1))
    
    # Sum over the specified period
    sum_tr = tr.rolling(window=period, min_periods=1).sum()
    sum_plus_vm = plus_vm.rolling(window=period, min_periods=1).sum()
    sum_minus_vm = minus_vm.rolling(window=period, min_periods=1).sum()
    
    # Calculate +VI and -VI as Series
    plus_vi = (sum_plus_vm / sum_tr).fillna(0)
    minus_vi = (sum_minus_vm / sum_tr).fillna(0)
    
    # Assign results to DataFrame
    data['+VI'] = plus_vi
    data['-VI'] = minus_vi
    
    return data

# Apply Vortex Indicator calculation
period = 14
data = calculate_vortex(data, period)

# Step 3: Plot Close Price and Vortex Indicator
plt.figure(figsize=(14, 7))

# Plot Close Price
plt.subplot(2, 1, 1)
plt.plot(data['Close'], label='Close Price', color='blue')
plt.title(f'{symbol} Close Price')
plt.xlabel('Date')
plt.ylabel('Price')
plt.legend()
plt.grid(True)

# Plot Vortex Indicator
plt.subplot(2, 1, 2)
plt.plot(data['+VI'], label='+VI (Positive Vortex)', color='green', linewidth=1.5)
plt.plot(data['-VI'], label='-VI (Negative Vortex)', color='red', linewidth=1.5)
plt.title(f'Vortex Indicator (VI) for {symbol}')
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

    /tmp/ipykernel_1218273/661315350.py in ?()
         40     return data
         41 
         42 # Apply Vortex Indicator calculation
         43 period = 14
    ---> 44 data = calculate_vortex(data, period)
         45 
         46 # Step 3: Plot Close Price and Vortex Indicator
         47 plt.figure(figsize=(14, 7))


    /tmp/ipykernel_1218273/661315350.py in ?(data, period)
         33     plus_vi = (sum_plus_vm / sum_tr).fillna(0)
         34     minus_vi = (sum_minus_vm / sum_tr).fillna(0)
         35 
         36     # Assign results to DataFrame
    ---> 37     data['+VI'] = plus_vi
         38     data['-VI'] = minus_vi
         39 
         40     return data


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


    ValueError: Cannot set a DataFrame with multiple columns to the single column +VI



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