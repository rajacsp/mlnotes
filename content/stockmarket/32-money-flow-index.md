---
title: 32-Money-Flow-Index
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

# Step 2: Calculate Money Flow Index (MFI)
def calculate_mfi(data, period=14):
    # Calculate Typical Price (TP) as a single Series
    data['Typical Price'] = (data['High'] + data['Low'] + data['Close']) / 3
    
    # Calculate Raw Money Flow (RMF)
    data['Raw Money Flow'] = data['Typical Price'] * data['Volume']
    
    # Identify Positive and Negative Money Flows
    data['Positive Money Flow'] = data['Raw Money Flow'].where(data['Typical Price'] > data['Typical Price'].shift(1), 0)
    data['Negative Money Flow'] = data['Raw Money Flow'].where(data['Typical Price'] < data['Typical Price'].shift(1), 0)
    
    # Calculate Money Flow Ratio (MFR)
    sum_positive = data['Positive Money Flow'].rolling(window=period).sum()
    sum_negative = data['Negative Money Flow'].rolling(window=period).sum()
    data['Money Flow Ratio'] = sum_positive / sum_negative
    
    # Calculate MFI
    data['MFI'] = 100 - (100 / (1 + data['Money Flow Ratio']))
    
    return data

# Apply MFI calculation
data = calculate_mfi(data)

# Step 3: Plot Close Price and MFI
plt.figure(figsize=(14, 7))

# Plot Close Price
plt.subplot(2, 1, 1)
plt.plot(data['Close'], label='Close Price', color='blue')
plt.title(f'{symbol} Close Price')
plt.xlabel('Date')
plt.ylabel('Price')
plt.legend()
plt.grid(True)

# Plot MFI
plt.subplot(2, 1, 2)
plt.plot(data['MFI'], label='MFI (Money Flow Index)', color='green', linewidth=1.5)
plt.axhline(80, color='red', linestyle='--', linewidth=1, label='Overbought (80)')
plt.axhline(20, color='blue', linestyle='--', linewidth=1, label='Oversold (20)')
plt.title(f'Money Flow Index (MFI) for {symbol}')
plt.xlabel('Date')
plt.ylabel('MFI')
plt.legend(loc='best')
plt.grid(True)

plt.tight_layout()
plt.show()
```

    [*********************100%***********************]  1 of 1 completed



    ---------------------------------------------------------------------------

    ValueError                                Traceback (most recent call last)

    /tmp/ipykernel_1248056/1062155594.py in ?()
         30 
         31     return data
         32 
         33 # Apply MFI calculation
    ---> 34 data = calculate_mfi(data)
         35 
         36 # Step 3: Plot Close Price and MFI
         37 plt.figure(figsize=(14, 7))


    /tmp/ipykernel_1248056/1062155594.py in ?(data, period)
         13     # Calculate Typical Price (TP) as a single Series
         14     data['Typical Price'] = (data['High'] + data['Low'] + data['Close']) / 3
         15 
         16     # Calculate Raw Money Flow (RMF)
    ---> 17     data['Raw Money Flow'] = data['Typical Price'] * data['Volume']
         18 
         19     # Identify Positive and Negative Money Flows
         20     data['Positive Money Flow'] = data['Raw Money Flow'].where(data['Typical Price'] > data['Typical Price'].shift(1), 0)


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


    ValueError: Cannot set a DataFrame with multiple columns to the single column Raw Money Flow



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