---
title: 35-Detrended-Price-Oscillator
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

# Step 2: Calculate Detrended Price Oscillator (DPO)
def calculate_dpo(data, period=20):
    # Calculate SMA as a single Series
    data['SMA'] = data['Close'].rolling(window=period, min_periods=1).mean()
    
    # Shift SMA by (period / 2) + 1
    data['Shifted SMA'] = data['SMA'].shift(int(period / 2) + 1)
    
    # Calculate DPO as a single Series
    data['DPO'] = data['Close'] - data['Shifted SMA']
    
    return data

# Apply DPO calculation
data = calculate_dpo(data)

# Step 3: Plot Close Price and DPO
plt.figure(figsize=(14, 7))

# Plot Close Price
plt.subplot(2, 1, 1)
plt.plot(data['Close'], label='Close Price', color='blue')
plt.title(f'{symbol} Close Price')
plt.xlabel('Date')
plt.ylabel('Price')
plt.legend()
plt.grid(True)

# Plot DPO
plt.subplot(2, 1, 2)
plt.plot(data['DPO'], label='Detrended Price Oscillator (DPO)', color='purple', linewidth=1.5)
plt.axhline(0, color='black', linestyle='--', linewidth=1, label='Zero Line')
plt.title(f'Detrended Price Oscillator (DPO) for {symbol}')
plt.xlabel('Date')
plt.ylabel('DPO')
plt.legend(loc='best')
plt.grid(True)

plt.tight_layout()
plt.show()
```

    [*********************100%***********************]  1 of 1 completed



    ---------------------------------------------------------------------------

    ValueError                                Traceback (most recent call last)

    /tmp/ipykernel_1262328/1687021974.py in ?()
         21 
         22     return data
         23 
         24 # Apply DPO calculation
    ---> 25 data = calculate_dpo(data)
         26 
         27 # Step 3: Plot Close Price and DPO
         28 plt.figure(figsize=(14, 7))


    /tmp/ipykernel_1262328/1687021974.py in ?(data, period)
         16     # Shift SMA by (period / 2) + 1
         17     data['Shifted SMA'] = data['SMA'].shift(int(period / 2) + 1)
         18 
         19     # Calculate DPO as a single Series
    ---> 20     data['DPO'] = data['Close'] - data['Shifted SMA']
         21 
         22     return data


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


    ValueError: Cannot set a DataFrame with multiple columns to the single column DPO



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