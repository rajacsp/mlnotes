---
title: 49-Renko-Point-Chart
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
from stocktrends import Renko
import matplotlib.pyplot as plt

# Step 1: Download historical data
symbol = "^GSPC"
start = "2020-01-01"
end = "2023-12-31"
data = yf.download(symbol, start=start, end=end)

# Step 2: Prepare data for Renko chart
renko_data = data[['Close']].reset_index()
renko_data.columns = ['date', 'close']

# Step 3: Create Renko chart
renko = Renko(renko_data)
renko.brick_size = 50  # Set the brick size
renko_chart = renko.get_ohlc_data()

# Step 4: Plot Renko chart
plt.figure(figsize=(14, 7))
plt.plot(renko_chart['date'], renko_chart['uptrend'], label='Uptrend', color='green', linewidth=2)
plt.plot(renko_chart['date'], renko_chart['downtrend'], label='Downtrend', color='red', linewidth=2)
plt.title(f'{symbol} Renko Chart (Brick Size: 50)')
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

    Cell In[4], line 17
         14 renko_data.columns = ['date', 'close']
         16 # Step 3: Create Renko chart
    ---> 17 renko = Renko(renko_data)
         18 renko.brick_size = 50  # Set the brick size
         19 renko_chart = renko.get_ohlc_data()


    File ~/miniconda3/envs/ml312-2024/lib/python3.12/site-packages/stocktrends/indicators.py:11, in Instrument.__init__(self, df)
          9 self.odf = df
         10 self.df = df
    ---> 11 self._validate_df()


    File ~/miniconda3/envs/ml312-2024/lib/python3.12/site-packages/stocktrends/indicators.py:22, in Instrument._validate_df(self)
         20 def _validate_df(self):
         21     if not self.ohlc.issubset(self.df.columns):
    ---> 22         raise ValueError('DataFrame should have OHLC {} columns'.format(self.ohlc))


    ValueError: DataFrame should have OHLC {'high', 'open', 'low', 'close'} columns



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