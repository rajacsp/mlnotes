---
title: 23-Pivot-Points
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
# Step 2: Calculate Pivot Points
def calculate_pivot_points(data):
    high = data['High']
    low = data['Low']
    close = data['Close']
    
    # Calculate pivot levels as single Series
    pivot = (high + low + close) / 3
    r1 = 2 * pivot - low
    s1 = 2 * pivot - high
    r2 = pivot + (high - low)
    s2 = pivot - (high - low)
    r3 = r2 + (high - low)
    s3 = s2 - (high - low)
    
    # Assign pivot levels to the DataFrame
    data['Pivot'] = pivot
    data['R1'] = r1
    data['S1'] = s1
    data['R2'] = r2
    data['S2'] = s2
    data['R3'] = r3
    data['S3'] = s3
    
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
    
    # Apply the pivot point calculation
    data = calculate_pivot_points(data)
    
    # Step 3: Plot Close Price and Pivot Points
    plt.figure(figsize=(14, 7))
    plt.plot(data['Close'], label='Close Price', color='blue', alpha=0.6)
    
    # Plot pivot points
    plt.axhline(data['Pivot'].iloc[-1], linestyle='--', color='black', label='Pivot (PP)')
    plt.axhline(data['R1'].iloc[-1], linestyle='--', color='green', label='Resistance R1')
    plt.axhline(data['S1'].iloc[-1], linestyle='--', color='red', label='Support S1')
    plt.axhline(data['R2'].iloc[-1], linestyle='--', color='darkgreen', label='Resistance R2')
    plt.axhline(data['S2'].iloc[-1], linestyle='--', color='darkred', label='Support S2')
    plt.axhline(data['R3'].iloc[-1], linestyle='--', color='lightgreen', label='Resistance R3')
    plt.axhline(data['S3'].iloc[-1], linestyle='--', color='pink', label='Support S3')
    
    plt.title(f'Pivot Points for {symbol}')
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



    
![png](/mlnotes/images/23-pivot-points_7_1.png)
    



```python

```


---
**Score: 5**