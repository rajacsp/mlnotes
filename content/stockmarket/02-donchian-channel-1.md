---
title: 02-Donchian-Channel-1
date: 2025-05-17
author: Your Name
cell_count: 6
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

# Step 2: Calculate Donchian Channels
def donchian_channels(data, window=20):
    data['Upper Band'] = data['High'].rolling(window=window).max()
    data['Lower Band'] = data['Low'].rolling(window=window).min()
    data['Middle Band'] = (data['Upper Band'] + data['Lower Band']) / 2
    return data

# Apply Donchian Channel function
data = donchian_channels(data)

# Step 3: Plot the data with Donchian Channels
plt.figure(figsize=(14, 7))
plt.plot(data['Close'], label='Close Price', color='blue')
plt.plot(data['Upper Band'], label='Upper Band', color='red', linestyle='--')
plt.plot(data['Lower Band'], label='Lower Band', color='green', linestyle='--')
plt.plot(data['Middle Band'], label='Middle Band', color='orange', linestyle='-.')
plt.fill_between(data.index, data['Lower Band'], data['Upper Band'], color='gray', alpha=0.2)
plt.title(f'Donchian Channels for {symbol}')
plt.xlabel('Date')
plt.ylabel('Price')
plt.legend(loc='best')
plt.grid(True)
plt.show()
```

    [*********************100%***********************]  1 of 1 completed



    
![png](/mlnotes/images/02-donchian-channel-1_4_1.png)
    



```python

```


---
**Score: 5**