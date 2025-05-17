---
title: 40-Zigzag-Indicator
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
from scipy.signal import argrelextrema

# Step 1: Download historical data
symbol = "^GSPC"  # S&P 500 as an example
start = "2020-01-01"
end = "2023-12-31"
data = yf.download(symbol, start=start, end=end)

# Step 2: Calculate ZigZag Indicator
def calculate_zigzag(data, threshold=5):
    # Identify local maxima and minima
    data['Local Max'] = data['Close'][argrelextrema(data['Close'].values, comparator=np.greater, order=5)[0]]
    data['Local Min'] = data['Close'][argrelextrema(data['Close'].values, comparator=np.less, order=5)[0]]
    
    # Combine maxima and minima
    turning_points = pd.concat([data['Local Max'].dropna(), data['Local Min'].dropna()])
    turning_points = turning_points.sort_index()
    
    # Filter significant changes
    zigzag = []
    last_value = None
    for index, value in turning_points.items():
        if last_value is None or abs((value - last_value) / last_value * 100) >= threshold:
            zigzag.append((index, value))
            last_value = value
    
    zigzag_df = pd.DataFrame(zigzag, columns=['Date', 'Value']).set_index('Date')
    return zigzag_df

# Apply ZigZag calculation
threshold = 5  # Define the percentage change threshold
zigzag = calculate_zigzag(data, threshold)

# Step 3: Plot Close Price and ZigZag Indicator
plt.figure(figsize=(14, 7))

# Plot Close Price
plt.plot(data['Close'], label='Close Price', color='blue', linewidth=1)
plt.scatter(zigzag.index, zigzag['Value'], color='red', label='ZigZag Turning Points', zorder=3)
plt.plot(zigzag['Value'], color='green', linestyle='--', linewidth=1, label='ZigZag Line')

plt.title(f'{symbol} ZigZag Indicator (Threshold: {threshold}%)')
plt.xlabel('Date')
plt.ylabel('Price')
plt.legend(loc='best')
plt.grid(True)

plt.tight_layout()
plt.show()
```

    [*********************100%***********************]  1 of 1 completed



    ---------------------------------------------------------------------------

    KeyError                                  Traceback (most recent call last)

    Cell In[5], line 35
         33 # Apply ZigZag calculation
         34 threshold = 5  # Define the percentage change threshold
    ---> 35 zigzag = calculate_zigzag(data, threshold)
         37 # Step 3: Plot Close Price and ZigZag Indicator
         38 plt.figure(figsize=(14, 7))


    Cell In[5], line 15, in calculate_zigzag(data, threshold)
         13 def calculate_zigzag(data, threshold=5):
         14     # Identify local maxima and minima
    ---> 15     data['Local Max'] = data['Close'][argrelextrema(data['Close'].values, comparator=np.greater, order=5)[0]]
         16     data['Local Min'] = data['Close'][argrelextrema(data['Close'].values, comparator=np.less, order=5)[0]]
         18     # Combine maxima and minima


    File ~/miniconda3/envs/ml312-2024/lib/python3.12/site-packages/pandas/core/frame.py:4108, in DataFrame.__getitem__(self, key)
       4106     if is_iterator(key):
       4107         key = list(key)
    -> 4108     indexer = self.columns._get_indexer_strict(key, "columns")[1]
       4110 # take() does not accept boolean indexers
       4111 if getattr(indexer, "dtype", None) == bool:


    File ~/miniconda3/envs/ml312-2024/lib/python3.12/site-packages/pandas/core/indexes/base.py:6200, in Index._get_indexer_strict(self, key, axis_name)
       6197 else:
       6198     keyarr, indexer, new_indexer = self._reindex_non_unique(keyarr)
    -> 6200 self._raise_if_missing(keyarr, indexer, axis_name)
       6202 keyarr = self.take(indexer)
       6203 if isinstance(key, Index):
       6204     # GH 42790 - Preserve name from an Index


    File ~/miniconda3/envs/ml312-2024/lib/python3.12/site-packages/pandas/core/indexes/base.py:6249, in Index._raise_if_missing(self, key, indexer, axis_name)
       6247 if nmissing:
       6248     if nmissing == len(indexer):
    -> 6249         raise KeyError(f"None of [{key}] are in the [{axis_name}]")
       6251     not_found = list(ensure_index(key)[missing_mask.nonzero()[0]].unique())
       6252     raise KeyError(f"{not_found} not in index")


    KeyError: "None of [Index([  11,   32,   42,   58,   73,   81,  108,  119,  139,  169,  177,  196,\n        221,  236,  243,  257,  267,  281,  303,  324,  333,  339,  364,  383,\n        393,  408,  421,  436,  467,  475,  490,  505,  512,  526,  545,  564,\n        578,  589,  598,  609,  624,  632,  660,  678,  694,  712,  722,  734,\n        743,  777,  786,  798,  809,  818,  828,  836,  850,  869,  880,  899,\n        923,  931,  950, 1004],\n      dtype='int64', name='Ticker')] are in the [columns]"



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