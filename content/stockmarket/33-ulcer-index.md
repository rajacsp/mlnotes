---
title: 33-Ulcer-Index
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

# Step 2: Calculate Ulcer Index (UI)
def calculate_ulcer_index(data, period=14):
    # Calculate rolling maximum
    data['Rolling Max'] = data['Close'].rolling(window=period, min_periods=1).max()
    
    # Calculate percentage drawdown
    data['Drawdown'] = ((data['Close'] - data['Rolling Max']) / data['Rolling Max']) * 100
    
    # Calculate Ulcer Index (UI)
    data['Drawdown Squared'] = data['Drawdown']**2
    data['Ulcer Index'] = np.sqrt(data['Drawdown Squared'].rolling(window=period, min_periods=1).mean())
    
    return data

# Apply Ulcer Index calculation
data = calculate_ulcer_index(data)

# Step 3: Plot Close Price and Ulcer Index
plt.figure(figsize=(14, 7))

# Plot Close Price
plt.subplot(2, 1, 1)
plt.plot(data['Close'], label='Close Price', color='blue')
plt.title(f'{symbol} Close Price')
plt.xlabel('Date')
plt.ylabel('Price')
plt.legend()
plt.grid(True)

# Plot Ulcer Index
plt.subplot(2, 1, 2)
plt.plot(data['Ulcer Index'], label='Ulcer Index (UI)', color='red', linewidth=1.5)
plt.title(f'Ulcer Index (UI) for {symbol}')
plt.xlabel('Date')
plt.ylabel('Ulcer Index')
plt.legend(loc='best')
plt.grid(True)

plt.tight_layout()
plt.show()
```

    [*********************100%***********************]  1 of 1 completed



    ---------------------------------------------------------------------------

    ValueError                                Traceback (most recent call last)

    /tmp/ipykernel_1250259/2210956523.py in ?()
         23 
         24     return data
         25 
         26 # Apply Ulcer Index calculation
    ---> 27 data = calculate_ulcer_index(data)
         28 
         29 # Step 3: Plot Close Price and Ulcer Index
         30 plt.figure(figsize=(14, 7))


    /tmp/ipykernel_1250259/2210956523.py in ?(data, period)
         14     # Calculate rolling maximum
         15     data['Rolling Max'] = data['Close'].rolling(window=period, min_periods=1).max()
         16 
         17     # Calculate percentage drawdown
    ---> 18     data['Drawdown'] = ((data['Close'] - data['Rolling Max']) / data['Rolling Max']) * 100
         19 
         20     # Calculate Ulcer Index (UI)
         21     data['Drawdown Squared'] = data['Drawdown']**2


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


    ValueError: Cannot set a DataFrame with multiple columns to the single column Drawdown



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