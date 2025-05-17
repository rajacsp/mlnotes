---
title: 14-Accumulation-Distribution-Line
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
import yfinance as yf
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
```


```python
# Step 2: Calculate A/D Line
def calculate_ad_line(data):
    # Calculate Money Flow Multiplier (MFM)
    mfm = ((data['Close'] - data['Low']) - (data['High'] - data['Close'])) / (data['High'] - data['Low'])
    mfm = mfm.fillna(0)  # Handle division by zero or missing data
    
    # Calculate Money Flow Volume (MFV)
    mfv = mfm * data['Volume']
    
    # Calculate A/D Line
    data['A/D Line'] = mfv.cumsum()
    
    return data
```


```python

```


```python
def show_graph(symbol):

    # Step 1: Download historical data
    start = "2020-01-01"
    end = "2024-12-31"
    data = yf.download(symbol, start=start, end=end)
    
    # Apply the A/D Line calculation
    data = calculate_ad_line(data)
    
    # Step 3: Plot A/D Line
    plt.figure(figsize=(14, 7))
    
    # Plot Close Price
    plt.subplot(2, 1, 1)
    plt.plot(data['Close'], label='Close Price', color='blue')
    plt.title(f'{symbol} Close Price')
    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.legend()
    plt.grid(True)
    
    # Plot A/D Line
    plt.subplot(2, 1, 2)
    plt.plot(data['A/D Line'], label='A/D Line', color='green')
    plt.title('Accumulation/Distribution Line (A/D Line)')
    plt.xlabel('Date')
    plt.ylabel('A/D Value')
    plt.legend(loc='best')
    plt.grid(True)
    
    plt.tight_layout()
    plt.show()
```


```python
show_graph("AMZN")
```

    [*********************100%***********************]  1 of 1 completed


```python

```


---
**Score: 5**