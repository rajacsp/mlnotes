---
title: 19-Renko-Charts
date: 2025-05-17
author: Your Name
cell_count: 10
score: 10
---

```python
# Created: 20250103
```


```python
import pyutil as pyu
pyu.get_local_pyinfo()
```




    'conda env: ml312-2024; pyv: 3.12.7 | packaged by Anaconda, Inc. | (main, Oct  4 2024, 13:27:36) [GCC 11.2.0]'




```python
# !pip install stocktrends
```


```python
print(pyu.ps2("stocktrends yfinance pandas matplotlib"))
```

    stocktrends==0.1.5
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
from stocktrends import Renko
import matplotlib.pyplot as plt

# Step 1: Download historical data
symbol = "^GSPC"  # S&P 500 as an example
start = "2020-01-01"
end = "2023-12-31"
data = yf.download(symbol, start=start, end=end)

# Step 2: Prepare data for Renko
def prepare_renko_data(data, brick_size=50):
    # Rename columns to lowercase as required by the Renko library
    data_renko = data[['Open', 'High', 'Low', 'Close']].copy()
    data_renko.columns = ['open', 'high', 'low', 'close']
    data_renko.reset_index(inplace=True)
    
    # Initialize Renko object
    renko = Renko(data_renko)
    renko.brick_size = brick_size  # Set the brick size
    renko_data = renko.get_ohlc_data()  # Generate Renko bricks
    
    # Add approximate dates from original data index
    renko_data['date'] = data_renko['date'].iloc[:len(renko_data)].reset_index(drop=True)
    
    return renko_data

# Step 3: Generate Renko data
brick_size = 50  # Adjust brick size as needed
renko_data = prepare_renko_data(data, brick_size)

# Step 4: Plot Renko Chart
plt.figure(figsize=(14, 7))
plt.plot(renko_data['date'], renko_data['open'], marker='o', linestyle='-', color='green', label='Open')
plt.plot(renko_data['date'], renko_data['close'], marker='o', linestyle='-', color='red', label='Close')
plt.fill_between(renko_data['date'], renko_data['open'], renko_data['close'], 
                 where=renko_data['close'] >= renko_data['open'], facecolor='green', alpha=0.4)
plt.fill_between(renko_data['date'], renko_data['open'], renko_data['close'], 
                 where=renko_data['close'] < renko_data['open'], facecolor='red', alpha=0.4)
plt.title(f'Renko Chart for {symbol} (Brick Size = {brick_size})')
plt.xlabel('Date')
plt.ylabel('Price')
plt.legend(loc='best')
plt.grid(True)
plt.show()
```

    [*********************100%***********************]  1 of 1 completed



    ---------------------------------------------------------------------------

    KeyError                                  Traceback (most recent call last)

    Cell In[14], line 31
         29 # Step 3: Generate Renko data
         30 brick_size = 50  # Adjust brick size as needed
    ---> 31 renko_data = prepare_renko_data(data, brick_size)
         33 # Step 4: Plot Renko Chart
         34 plt.figure(figsize=(14, 7))


    Cell In[14], line 22, in prepare_renko_data(data, brick_size)
         20 renko = Renko(data_renko)
         21 renko.brick_size = brick_size  # Set the brick size
    ---> 22 renko_data = renko.get_ohlc_data()  # Generate Renko bricks
         24 # Add approximate dates from original data index
         25 renko_data['date'] = data_renko['date'].iloc[:len(renko_data)].reset_index(drop=True)


    File ~/miniconda3/envs/ml312-2024/lib/python3.12/site-packages/stocktrends/indicators.py:37, in Renko.get_ohlc_data(self)
         35 def get_ohlc_data(self):
         36     if self.chart_type == self.PERIOD_CLOSE:
    ---> 37         self.period_close_bricks()
         38     else:
         39         self.price_movement_bricks()


    File ~/miniconda3/envs/ml312-2024/lib/python3.12/site-packages/stocktrends/indicators.py:49, in Renko.period_close_bricks(self)
         47 brick_size = self.brick_size
         48 columns = ['date', 'open', 'high', 'low', 'close']
    ---> 49 self.df = self.df[columns]
         51 self.cdf = pd.DataFrame(
         52     columns=columns,
         53     data=[],
         54 )
         56 self.cdf.loc[0] = self.df.loc[0]


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


    File ~/miniconda3/envs/ml312-2024/lib/python3.12/site-packages/pandas/core/indexes/base.py:6252, in Index._raise_if_missing(self, key, indexer, axis_name)
       6249     raise KeyError(f"None of [{key}] are in the [{axis_name}]")
       6251 not_found = list(ensure_index(key)[missing_mask.nonzero()[0]].unique())
    -> 6252 raise KeyError(f"{not_found} not in index")


    KeyError: "['date'] not in index"



```python

```


```python
def show_graph(symbol):

pass
```


```python
show_graph("AMZN")
```

    [*********************100%***********************]  1 of 1 completed



    
![png](/mlnotes/images/19-renko-charts_8_1.png)
    



```python

```


---
**Score: 10**