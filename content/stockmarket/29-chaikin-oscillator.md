---
title: 29-Chaikin-Oscillator
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

# Step 2: Calculate Chaikin Oscillator
def calculate_chaikin_oscillator(data, short_period=3, long_period=10):
    # Money Flow Multiplier (MFM)
    data['MFM'] = ((data['Close'] - data['Low']) - (data['High'] - data['Close'])) / (data['High'] - data['Low'])
    data['MFM'].replace([np.inf, -np.inf], 0, inplace=True)  # Handle division by zero
    data['MFM'].fillna(0, inplace=True)
    
    # Money Flow Volume (MFV)
    data['MFV'] = data['MFM'] * data['Volume']
    
    # Accumulation/Distribution (A/D) Line
    data['A/D Line'] = data['MFV'].cumsum()
    
    # Chaikin Oscillator
    data['Chaikin Oscillator'] = (
        data['A/D Line'].ewm(span=short_period, adjust=False).mean() -
        data['A/D Line'].ewm(span=long_period, adjust=False).mean()
    )
    
    return data

# Apply Chaikin Oscillator calculation
data = calculate_chaikin_oscillator(data)

# Step 3: Plot Close Price and Chaikin Oscillator
plt.figure(figsize=(14, 7))

# Plot Close Price
plt.subplot(2, 1, 1)
plt.plot(data['Close'], label='Close Price', color='blue')
plt.title(f'{symbol} Close Price')
plt.xlabel('Date')
plt.ylabel('Price')
plt.legend()
plt.grid(True)

# Plot Chaikin Oscillator
plt.subplot(2, 1, 2)
plt.plot(data['Chaikin Oscillator'], label='Chaikin Oscillator', color='purple', linewidth=1.5)
plt.axhline(0, color='black', linestyle='--', linewidth=1, label='Zero Line')
plt.title(f'Chaikin Oscillator for {symbol}')
plt.xlabel('Date')
plt.ylabel('Value')
plt.legend(loc='best')
plt.grid(True)

plt.tight_layout()
plt.show()
```

    [*********************100%***********************]  1 of 1 completed
    /tmp/ipykernel_1226199/284241031.py:15: SettingWithCopyWarning: 
    A value is trying to be set on a copy of a slice from a DataFrame
    
    See the caveats in the documentation: https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#returning-a-view-versus-a-copy
      data['MFM'].replace([np.inf, -np.inf], 0, inplace=True)  # Handle division by zero
    /tmp/ipykernel_1226199/284241031.py:16: SettingWithCopyWarning: 
    A value is trying to be set on a copy of a slice from a DataFrame
    
    See the caveats in the documentation: https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#returning-a-view-versus-a-copy
      data['MFM'].fillna(0, inplace=True)



    ---------------------------------------------------------------------------

    ValueError                                Traceback (most recent call last)

    /tmp/ipykernel_1226199/284241031.py in ?()
         29 
         30     return data
         31 
         32 # Apply Chaikin Oscillator calculation
    ---> 33 data = calculate_chaikin_oscillator(data)
         34 
         35 # Step 3: Plot Close Price and Chaikin Oscillator
         36 plt.figure(figsize=(14, 7))


    /tmp/ipykernel_1226199/284241031.py in ?(data, short_period, long_period)
         15     data['MFM'].replace([np.inf, -np.inf], 0, inplace=True)  # Handle division by zero
         16     data['MFM'].fillna(0, inplace=True)
         17 
         18     # Money Flow Volume (MFV)
    ---> 19     data['MFV'] = data['MFM'] * data['Volume']
         20 
         21     # Accumulation/Distribution (A/D) Line
         22     data['A/D Line'] = data['MFV'].cumsum()


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


    ValueError: Cannot set a DataFrame with multiple columns to the single column MFV



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