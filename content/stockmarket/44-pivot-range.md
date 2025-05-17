---
title: 44-Pivot-Range
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

# Step 2: Calculate Pivot Range
def calculate_pivot_range(data):
    data['Pivot Point'] = (data['High'] + data['Low'] + data['Close']) / 3
    data['R1'] = 2 * data['Pivot Point'] - data['Low']
    data['R2'] = data['Pivot Point'] + (data['High'] - data['Low'])
    data['S1'] = 2 * data['Pivot Point'] - data['High']
    data['S2'] = data['Pivot Point'] - (data['High'] - data['Low'])
    return data

# Apply Pivot Range calculation
data = calculate_pivot_range(data)

# Step 3: Plot Close Price and Pivot Range
plt.figure(figsize=(14, 7))

# Plot Close Price
plt.plot(data['Close'], label='Close Price', color='blue', linewidth=1)
plt.plot(data['Pivot Point'], label='Pivot Point (P)', color='black', linestyle='--')
plt.plot(data['R1'], label='Resistance 1 (R1)', color='green', linestyle='--')
plt.plot(data['R2'], label='Resistance 2 (R2)', color='lime', linestyle='--')
plt.plot(data['S1'], label='Support 1 (S1)', color='red', linestyle='--')
plt.plot(data['S2'], label='Support 2 (S2)', color='orange', linestyle='--')

# Customize the plot
plt.title(f'{symbol} Pivot Range')
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

    /tmp/ipykernel_1326968/2158972586.py in ?()
         17     data['S2'] = data['Pivot Point'] - (data['High'] - data['Low'])
         18     return data
         19 
         20 # Apply Pivot Range calculation
    ---> 21 data = calculate_pivot_range(data)
         22 
         23 # Step 3: Plot Close Price and Pivot Range
         24 plt.figure(figsize=(14, 7))


    /tmp/ipykernel_1326968/2158972586.py in ?(data)
         12 def calculate_pivot_range(data):
         13     data['Pivot Point'] = (data['High'] + data['Low'] + data['Close']) / 3
    ---> 14     data['R1'] = 2 * data['Pivot Point'] - data['Low']
         15     data['R2'] = data['Pivot Point'] + (data['High'] - data['Low'])
         16     data['S1'] = 2 * data['Pivot Point'] - data['High']
         17     data['S2'] = data['Pivot Point'] - (data['High'] - data['Low'])


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


    ValueError: Cannot set a DataFrame with multiple columns to the single column R1



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