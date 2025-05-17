---
title: 50-Heikin-Ashi-Candles
date: 2025-05-17
author: Your Name
cell_count: 10
score: 10
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
# !pip install mplfinance
```


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
import mplfinance as mpf

# Step 1: Download historical data
symbol = "^GSPC"  # S&P 500 as an example
start = "2023-12-01"
end = "2023-12-31"
data = yf.download(symbol, start=start, end=end)

# Step 2: Calculate Heikin Ashi Candles
def calculate_heikin_ashi(data):
    ha_data = data[['Open', 'High', 'Low', 'Close']].copy()
    
    ha_data['HA Close'] = (data['Open'] + data['High'] + data['Low'] + data['Close']) / 4
    ha_data['HA Open'] = (data['Open'].shift(1) + data['Close'].shift(1)) / 2
    ha_data['HA High'] = ha_data[['High', 'HA Open', 'HA Close']].max(axis=1)
    ha_data['HA Low'] = ha_data[['Low', 'HA Open', 'HA Close']].min(axis=1)
    
    return ha_data[['HA Open', 'HA High', 'HA Low', 'HA Close']]

# Apply Heikin Ashi calculation
ha_data = calculate_heikin_ashi(data)

# Step 3: Plot Heikin Ashi Candles
ha_candles = ha_data.rename(columns={'HA Open': 'open', 'HA High': 'high', 'HA Low': 'low', 'HA Close': 'close'})
mpf.plot(ha_candles, type='candle', style='charles', title=f'{symbol} Heikin Ashi Candles', ylabel='Price', ylabel_lower='Volume')

```

    [*********************100%***********************]  1 of 1 completed



    ---------------------------------------------------------------------------

    ValueError                                Traceback (most recent call last)

    Cell In[13], line 28
         26 # Step 3: Plot Heikin Ashi Candles
         27 ha_candles = ha_data.rename(columns={'HA Open': 'open', 'HA High': 'high', 'HA Low': 'low', 'HA Close': 'close'})
    ---> 28 mpf.plot(ha_candles, type='candle', style='charles', title=f'{symbol} Heikin Ashi Candles', ylabel='Price', ylabel_lower='Volume')


    File ~/miniconda3/envs/ml312-2024/lib/python3.12/site-packages/mplfinance/plotting.py:533, in plot(data, **kwargs)
        531     pnf_results = _construct_pnf_scatter(axA1,ptype,dates,xdates,opens,highs,lows,closes,volumes,config,style)
        532 else:
    --> 533     collections =_construct_mpf_collections(ptype,dates,xdates,opens,highs,lows,closes,volumes,config,style)
        535 if ptype == 'pnf':
        536     volumes    = pnf_results['pnf_volumes']


    File ~/miniconda3/envs/ml312-2024/lib/python3.12/site-packages/mplfinance/_utils.py:93, in _construct_mpf_collections(ptype, dates, xdates, opens, highs, lows, closes, volumes, config, style)
         91 collections = None
         92 if ptype == 'candle' or ptype == 'candlestick':
    ---> 93     collections = _construct_candlestick_collections(xdates, opens, highs, lows, closes,
         94                                                      marketcolors=style['marketcolors'],config=config )
         96 elif ptype =='hollow_and_filled':
         97         collections = _construct_hollow_candlestick_collections(xdates, opens, highs, lows, closes,
         98                                                      marketcolors=style['marketcolors'],config=config )


    File ~/miniconda3/envs/ml312-2024/lib/python3.12/site-packages/mplfinance/_utils.py:665, in _construct_candlestick_collections(dates, opens, highs, lows, closes, marketcolors, config)
        637 def _construct_candlestick_collections(dates, opens, highs, lows, closes, marketcolors=None, config=None):
        638     """Represent the open, close as a bar line and high low range as a
        639     vertical line.
        640 
       (...)
        662         (lineCollection, barCollection)
        663     """
    --> 665     _check_input(opens, highs, lows, closes)
        667     if marketcolors is None:
        668         marketcolors = _get_mpfstyle('classic')['marketcolors']


    File ~/miniconda3/envs/ml312-2024/lib/python3.12/site-packages/mplfinance/_utils.py:58, in _check_input(opens, closes, highs, lows)
         56 same_numnans = len(o) == len(h) == len(l) == len(c)
         57 if not same_numnans:
    ---> 58     raise ValueError('O,H,L,C must have the same amount of missing data!')
         60 same_missing = ((o == h).all() and
         61                 (o == l).all() and
         62                 (o == c).all()
         63                )
         64 if not same_missing:


    ValueError: O,H,L,C must have the same amount of missing data!



    
![png](/mlnotes/images/50-heikin-ashi-candles_5_2.png)
    



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
**Score: 10**