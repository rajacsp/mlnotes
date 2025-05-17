---
title: 21-Triple-Exponential-Moving-Average
date: 2025-05-17
author: Your Name
cell_count: 9
score: 5
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
# Step 2: Calculate TEMA
def calculate_tema(data, period=20):
    # Calculate EMA1, EMA2, and EMA3
    ema1 = data['Close'].ewm(span=period, adjust=False).mean()
    ema2 = ema1.ewm(span=period, adjust=False).mean()
    ema3 = ema2.ewm(span=period, adjust=False).mean()
    
    # Calculate TEMA
    tema = 3 * ema1 - 3 * ema2 + ema3
    data['TEMA'] = tema
    return data
```


```python

```


```python
def show_graph(symbol):

    # Step 1: Download historical data
    start = "2020-01-01"
    end = "2023-12-31"
    data = yf.download(symbol, start=start, end=end)
    
    # Apply TEMA calculation
    period = 20  # You can adjust the period
    data = calculate_tema(data, period)
    
    # Step 3: Plot Close Price and TEMA
    plt.figure(figsize=(14, 7))
    plt.plot(data['Close'], label='Close Price', color='blue', alpha=0.6)
    plt.plot(data['TEMA'], label=f'TEMA ({period})', color='red', linewidth=2)
    plt.title(f'TEMA (Triple Exponential Moving Average) for {symbol}')
    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.legend(loc='best')
    plt.grid(True)
    plt.show()
```


```python
show_graph("AMZN")
```

    [*********************100%***********************]  1 of 1 completed



    
![png](/mlnotes/images/21-triple-exponential-moving-average_7_1.png)
    



```python

```


---
**Score: 5**