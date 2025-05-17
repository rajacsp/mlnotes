---
title: 42-Gann-Fans
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
import numpy as np

# Step 1: Download historical data
symbol = "^GSPC"  # S&P 500 as an example
start = "2020-01-01"
end = "2023-12-31"
data = yf.download(symbol, start=start, end=end)

# Step 2: Identify a pivot point (e.g., the most recent low)
pivot_date = data['Close'].idxmin()  # Recent low
pivot_price = data['Close'].min()
pivot_index = data.index.get_loc(pivot_date)

# Step 3: Define Gann angles
angles = {
    '1x1': 45,
    '2x1': 63.5,
    '1x2': 26.5,
    '3x1': 71.5,
    '1x3': 18.5,
}

# Step 4: Plot Gann Fans
plt.figure(figsize=(14, 7))
plt.plot(data['Close'], label='Close Price', color='blue', linewidth=1)
plt.scatter(pivot_date, pivot_price, color='red', label='Pivot Point', zorder=3)

# Draw Gann angles
for label, angle in angles.items():
    # Create x values from the pivot point
    x = np.arange(0, len(data) - pivot_index)
    y = pivot_price + x * np.tan(np.radians(angle))
    
    # Adjust y values to align with the index
    gann_x = data.index[pivot_index : pivot_index + len(x)]
    gann_y = y[:len(gann_x)]  # Ensure lengths match
    
    plt.plot(gann_x, gann_y, label=f'Gann Fan {label}', linestyle='--')

# Customize plot
plt.title(f'{symbol} Gann Fans')
plt.xlabel('Date')
plt.ylabel('Price')
plt.legend(loc='best')
plt.grid(True)
plt.tight_layout()
plt.show()
```

    [*********************100%***********************]  1 of 1 completed



    ---------------------------------------------------------------------------

    InvalidIndexError                         Traceback (most recent call last)

    Cell In[7], line 15
         13 pivot_date = data['Close'].idxmin()  # Recent low
         14 pivot_price = data['Close'].min()
    ---> 15 pivot_index = data.index.get_loc(pivot_date)
         17 # Step 3: Define Gann angles
         18 angles = {
         19     '1x1': 45,
         20     '2x1': 63.5,
       (...)
         23     '1x3': 18.5,
         24 }


    File ~/miniconda3/envs/ml312-2024/lib/python3.12/site-packages/pandas/core/indexes/datetimes.py:590, in DatetimeIndex.get_loc(self, key)
        582 def get_loc(self, key):
        583     """
        584     Get integer location for requested label
        585 
       (...)
        588     loc : int
        589     """
    --> 590     self._check_indexing_error(key)
        592     orig_key = key
        593     if is_valid_na_for_dtype(key, self.dtype):


    File ~/miniconda3/envs/ml312-2024/lib/python3.12/site-packages/pandas/core/indexes/base.py:6059, in Index._check_indexing_error(self, key)
       6055 def _check_indexing_error(self, key):
       6056     if not is_scalar(key):
       6057         # if key is not a scalar, directly raise an error (the code below
       6058         # would convert to numpy arrays and raise later any way) - GH29926
    -> 6059         raise InvalidIndexError(key)


    InvalidIndexError: Ticker
    ^GSPC   2020-03-23
    dtype: datetime64[ns]



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