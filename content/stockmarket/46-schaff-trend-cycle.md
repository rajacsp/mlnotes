---
title: 46-Schaff-Trend-Cycle
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
# Step 2: Calculate Schaff Trend Cycle (STC)
def calculate_stc(data, fast_period=12, slow_period=26, signal_period=9, stoch_period=10, stoch_ema_period=3):
    # MACD Line and Signal Line
    data['Fast EMA'] = data['Close'].ewm(span=fast_period, adjust=False).mean()
    data['Slow EMA'] = data['Close'].ewm(span=slow_period, adjust=False).mean()
    data['MACD Line'] = data['Fast EMA'] - data['Slow EMA']
    data['Signal Line'] = data['MACD Line'].ewm(span=signal_period, adjust=False).mean()
    
    # Stochastic of MACD
    data['Lowest MACD'] = data['MACD Line'].rolling(window=stoch_period).min()
    data['Highest MACD'] = data['MACD Line'].rolling(window=stoch_period).max()
    data['Stochastic MACD'] = ((data['MACD Line'] - data['Lowest MACD']) /
                               (data['Highest MACD'] - data['Lowest MACD'])) * 100
    
    # STC
    data['STC'] = data['Stochastic MACD'].ewm(span=stoch_ema_period, adjust=False).mean()
    
    return data
```

    [*********************100%***********************]  1 of 1 completed



    
![png](/mlnotes/images/46-schaff-trend-cycle_4_1.png)
    



```python

```


```python
def show_graph(symbol):

    # Step 1: Download historical data
    start = "2020-01-01"
    end = "2023-12-31"
    data = yf.download(symbol, start=start, end=end)
    
    # Apply STC calculation
    data = calculate_stc(data)
    
    # Step 3: Plot Close Price and STC
    plt.figure(figsize=(14, 7))
    
    # Plot Close Price
    plt.subplot(2, 1, 1)
    plt.plot(data['Close'], label='Close Price', color='blue')
    plt.title(f'{symbol} Close Price')
    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.legend()
    plt.grid(True)
    
    # Plot STC
    plt.subplot(2, 1, 2)
    plt.plot(data['STC'], label='Schaff Trend Cycle (STC)', color='green', linewidth=1.5)
    plt.axhline(75, color='red', linestyle='--', linewidth=1, label='Overbought (75)')
    plt.axhline(25, color='blue', linestyle='--', linewidth=1, label='Oversold (25)')
    plt.title(f'Schaff Trend Cycle (STC) for {symbol}')
    plt.xlabel('Date')
    plt.ylabel('STC')
    plt.legend(loc='best')
    plt.grid(True)
    
    plt.tight_layout()
    plt.show()
```


```python
show_graph("AMZN")
```

    [*********************100%***********************]  1 of 1 completed



    
![png](/mlnotes/images/46-schaff-trend-cycle_7_1.png)
    



```python

```


---
**Score: 5**