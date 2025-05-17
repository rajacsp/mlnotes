---
title: 26-Dmi-And-Adx
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

# Step 2: Calculate DMI and ADX
def calculate_dmi_adx(data, period=14):
    high = data['High']
    low = data['Low']
    close = data['Close']
    
    # Calculate True Range (TR)
    tr1 = high - low
    tr2 = abs(high - close.shift(1))
    tr3 = abs(low - close.shift(1))
    tr = pd.DataFrame({'TR1': tr1, 'TR2': tr2, 'TR3': tr3}).max(axis=1)
    
    # Calculate +DM and -DM
    plus_dm = high.diff()
    minus_dm = low.diff()
    plus_dm[plus_dm < 0] = 0
    minus_dm[minus_dm > 0] = 0
    minus_dm = abs(minus_dm)
    
    # Smooth TR, +DM, -DM
    atr = tr.rolling(window=period).mean()
    smoothed_plus_dm = plus_dm.rolling(window=period).mean()
    smoothed_minus_dm = minus_dm.rolling(window=period).mean()
    
    # Calculate +DI and -DI
    plus_di = (smoothed_plus_dm / atr) * 100
    minus_di = (smoothed_minus_dm / atr) * 100
    
    # Calculate DX and ADX
    dx = (abs(plus_di - minus_di) / (plus_di + minus_di)) * 100
    adx = dx.rolling(window=period).mean()
    
    # Assign results to DataFrame
    data['+DI'] = plus_di
    data['-DI'] = minus_di
    data['ADX'] = adx
    
    return data

# Apply DMI and ADX calculation
period = 14
data = calculate_dmi_adx(data, period)

# Step 3: Plot Close Price, +DI, -DI, and ADX
plt.figure(figsize=(14, 10))

# Plot Close Price
plt.subplot(3, 1, 1)
plt.plot(data['Close'], label='Close Price', color='blue')
plt.title(f'{symbol} Close Price')
plt.xlabel('Date')
plt.ylabel('Price')
plt.legend()
plt.grid(True)

# Plot +DI and -DI
plt.subplot(3, 1, 2)
plt.plot(data['+DI'], label='+DI', color='green')
plt.plot(data['-DI'], label='-DI', color='red')
plt.title(f'Directional Movement Index (+DI and -DI) for {symbol}')
plt.xlabel('Date')
plt.ylabel('Index Value')
plt.legend(loc='best')
plt.grid(True)

# Plot ADX
plt.subplot(3, 1, 3)
plt.plot(data['ADX'], label='ADX', color='purple')
plt.axhline(25, color='black', linestyle='--', linewidth=1, label='Trend Threshold (25)')
plt.title(f'Average Directional Index (ADX) for {symbol}')
plt.xlabel('Date')
plt.ylabel('ADX Value')
plt.legend(loc='best')
plt.grid(True)

plt.tight_layout()
plt.show()
```

    [*********************100%***********************]  1 of 1 completed



    ---------------------------------------------------------------------------

    ValueError                                Traceback (most recent call last)

    Cell In[6], line 53
         51 # Apply DMI and ADX calculation
         52 period = 14
    ---> 53 data = calculate_dmi_adx(data, period)
         55 # Step 3: Plot Close Price, +DI, -DI, and ADX
         56 plt.figure(figsize=(14, 10))


    Cell In[6], line 22, in calculate_dmi_adx(data, period)
         20 tr2 = abs(high - close.shift(1))
         21 tr3 = abs(low - close.shift(1))
    ---> 22 tr = pd.DataFrame({'TR1': tr1, 'TR2': tr2, 'TR3': tr3}).max(axis=1)
         24 # Calculate +DM and -DM
         25 plus_dm = high.diff()


    File ~/miniconda3/envs/ml312-2024/lib/python3.12/site-packages/pandas/core/frame.py:778, in DataFrame.__init__(self, data, index, columns, dtype, copy)
        772     mgr = self._init_mgr(
        773         data, axes={"index": index, "columns": columns}, dtype=dtype, copy=copy
        774     )
        776 elif isinstance(data, dict):
        777     # GH#38939 de facto copy defaults to False only in non-dict cases
    --> 778     mgr = dict_to_mgr(data, index, columns, dtype=dtype, copy=copy, typ=manager)
        779 elif isinstance(data, ma.MaskedArray):
        780     from numpy.ma import mrecords


    File ~/miniconda3/envs/ml312-2024/lib/python3.12/site-packages/pandas/core/internals/construction.py:503, in dict_to_mgr(data, index, columns, dtype, typ, copy)
        499     else:
        500         # dtype check to exclude e.g. range objects, scalars
        501         arrays = [x.copy() if hasattr(x, "dtype") else x for x in arrays]
    --> 503 return arrays_to_mgr(arrays, columns, index, dtype=dtype, typ=typ, consolidate=copy)


    File ~/miniconda3/envs/ml312-2024/lib/python3.12/site-packages/pandas/core/internals/construction.py:114, in arrays_to_mgr(arrays, columns, index, dtype, verify_integrity, typ, consolidate)
        111 if verify_integrity:
        112     # figure out the index, if necessary
        113     if index is None:
    --> 114         index = _extract_index(arrays)
        115     else:
        116         index = ensure_index(index)


    File ~/miniconda3/envs/ml312-2024/lib/python3.12/site-packages/pandas/core/internals/construction.py:667, in _extract_index(data)
        664         raise ValueError("Per-column arrays must each be 1-dimensional")
        666 if not indexes and not raw_lengths:
    --> 667     raise ValueError("If using all scalar values, you must pass an index")
        669 if have_series:
        670     index = union_indexes(indexes)


    ValueError: If using all scalar values, you must pass an index



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