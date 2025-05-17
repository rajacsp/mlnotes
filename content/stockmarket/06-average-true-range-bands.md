---
title: 06-Average-True-Range-Bands
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
print(pyu.ps2("requests"))
```

    requests==2.32.3
    



```python

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

# Step 2: Calculate ATR Bands
def atr_bands(data, atr_window=14, sma_window=20, multiplier=2):
    # Calculate True Range (TR)
    data['High-Low'] = data['High'] - data['Low']
    data['High-Close'] = abs(data['High'] - data['Close'].shift(1))
    data['Low-Close'] = abs(data['Low'] - data['Close'].shift(1))
    data['True Range'] = data[['High-Low', 'High-Close', 'Low-Close']].max(axis=1)
    
    # Calculate ATR
    data['ATR'] = data['True Range'].rolling(window=atr_window).mean()
    
    # Calculate SMA (Middle Line)
    data['SMA'] = data['Close'].rolling(window=sma_window).mean()
    
    # Calculate Upper and Lower Bands
    data['Upper Band'] = data['SMA'] + (multiplier * data['ATR'])
    data['Lower Band'] = data['SMA'] - (multiplier * data['ATR'])
    
    return data

# Apply the function
data = atr_bands(data)

# Step 3: Plot ATR Bands
plt.figure(figsize=(14, 7))
plt.plot(data['Close'], label='Close Price', color='blue')
plt.plot(data['Upper Band'], label='Upper Band', color='red', linestyle='--')
plt.plot(data['Lower Band'], label='Lower Band', color='green', linestyle='--')
plt.plot(data['SMA'], label='SMA (Middle Line)', color='orange', linestyle='-')
plt.fill_between(data.index, data['Lower Band'], data['Upper Band'], color='gray', alpha=0.2)
plt.title(f'ATR Bands for {symbol}')
plt.xlabel('Date')
plt.ylabel('Price')
plt.legend(loc='best')
plt.grid(True)
plt.show()
```

    [*********************100%***********************]  1 of 1 completed



    
![png](/mlnotes/images/06-average-true-range-bands_4_1.png)
    



```python

```


```python
def show_atr_bands(symbol):

    # Step 1: Download historical data
    start = "2020-01-01"
    end = "2023-12-31"
    data = yf.download(symbol, start=start, end=end)

    # Apply the function
    data = atr_bands(data)
    
    # Step 3: Plot ATR Bands
    plt.figure(figsize=(14, 7))
    plt.plot(data['Close'], label='Close Price', color='blue')
    plt.plot(data['Upper Band'], label='Upper Band', color='red', linestyle='--')
    plt.plot(data['Lower Band'], label='Lower Band', color='green', linestyle='--')
    plt.plot(data['SMA'], label='SMA (Middle Line)', color='orange', linestyle='-')
    plt.fill_between(data.index, data['Lower Band'], data['Upper Band'], color='gray', alpha=0.2)
    plt.title(f'ATR Bands for {symbol}')
    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.legend(loc='best')
    plt.grid(True)
    plt.show()
```


```python
show_atr_bands("AMZN")
```

    [*********************100%***********************]  1 of 1 completed



    
![png](/mlnotes/images/06-average-true-range-bands_7_1.png)
    



```python

```


---
**Score: 5**