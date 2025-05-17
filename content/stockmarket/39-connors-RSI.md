---
title: 39-Connors-Rsi
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
import numpy as np
import matplotlib.pyplot as plt

# Step 1: Download historical data
symbol = "^GSPC"  # S&P 500 as an example
start = "2020-01-01"
end = "2023-12-31"
data = yf.download(symbol, start=start, end=end)

# Step 2: Helper function to calculate RSI
def calculate_rsi(series, period):
    delta = series.diff(1)
    gain = delta.where(delta > 0, 0).rolling(window=period).mean()
    loss = -delta.where(delta < 0, 0).rolling(window=period).mean()
    rs = gain / loss
    return 100 - (100 / (1 + rs))

# Step 3: Calculate streak
def calculate_streak(data):
    streak = np.zeros(len(data))
    for i in range(1, len(data)):
        if data['Close'].iloc[i] > data['Close'].iloc[i - 1]:
            streak[i] = streak[i - 1] + 1
        elif data['Close'].iloc[i] < data['Close'].iloc[i - 1]:
            streak[i] = streak[i - 1] - 1
        else:
            streak[i] = 0
    data['Streak'] = streak
    return data

# Step 4: Calculate Connors RSI (CRSI)
def calculate_connors_rsi(data, rsi_period=3, streak_rsi_period=2, percent_rank_period=100):
    # Calculate RSI
    data['RSI'] = calculate_rsi(data['Close'], rsi_period)
    
    # Calculate Streak and Streak RSI
    data = calculate_streak(data)
    data['Streak RSI'] = calculate_rsi(data['Streak'], streak_rsi_period)
    
    # Calculate Percentage Rank
    data['Price Change'] = data['Close'].diff(1)
    data['Percent Rank'] = data['Price Change'].rolling(window=percent_rank_period).apply(
        lambda x: (x.rank(pct=True).iloc[-1]) * 100, raw=False
    )
    
    # Calculate Connors RSI
    data['Connors RSI'] = (data['RSI'] + data['Streak RSI'] + data['Percent Rank']) / 3
    return data

# Apply Connors RSI calculation
data = calculate_connors_rsi(data)

# Step 5: Plot Close Price and Connors RSI
plt.figure(figsize=(14, 7))

# Plot Close Price
plt.subplot(2, 1, 1)
plt.plot(data['Close'], label='Close Price', color='blue')
plt.title(f'{symbol} Close Price')
plt.xlabel('Date')
plt.ylabel('Price')
plt.legend()
plt.grid(True)

# Plot Connors RSI
plt.subplot(2, 1, 2)
plt.plot(data['Connors RSI'], label='Connors RSI', color='green', linewidth=1.5)
plt.axhline(70, color='red', linestyle='--', linewidth=1, label='Overbought (70)')
plt.axhline(30, color='blue', linestyle='--', linewidth=1, label='Oversold (30)')
plt.title(f'Connors RSI for {symbol}')
plt.xlabel('Date')
plt.ylabel('CRSI')
plt.legend(loc='best')
plt.grid(True)

plt.tight_layout()
plt.show()
```

    [*********************100%***********************]  1 of 1 completed



    ---------------------------------------------------------------------------

    ValueError                                Traceback (most recent call last)

    /tmp/ipykernel_1279737/2295550227.py in ?()
         49     data['Connors RSI'] = (data['RSI'] + data['Streak RSI'] + data['Percent Rank']) / 3
         50     return data
         51 
         52 # Apply Connors RSI calculation
    ---> 53 data = calculate_connors_rsi(data)
         54 
         55 # Step 5: Plot Close Price and Connors RSI
         56 plt.figure(figsize=(14, 7))


    /tmp/ipykernel_1279737/2295550227.py in ?(data, rsi_period, streak_rsi_period, percent_rank_period)
         35     # Calculate RSI
         36     data['RSI'] = calculate_rsi(data['Close'], rsi_period)
         37 
         38     # Calculate Streak and Streak RSI
    ---> 39     data = calculate_streak(data)
         40     data['Streak RSI'] = calculate_rsi(data['Streak'], streak_rsi_period)
         41 
         42     # Calculate Percentage Rank


    /tmp/ipykernel_1279737/2295550227.py in ?(data)
         21 def calculate_streak(data):
         22     streak = np.zeros(len(data))
         23     for i in range(1, len(data)):
    ---> 24         if data['Close'].iloc[i] > data['Close'].iloc[i - 1]:
         25             streak[i] = streak[i - 1] + 1
         26         elif data['Close'].iloc[i] < data['Close'].iloc[i - 1]:
         27             streak[i] = streak[i - 1] - 1


    ~/miniconda3/envs/ml312-2024/lib/python3.12/site-packages/pandas/core/generic.py in ?(self)
       1575     @final
       1576     def __nonzero__(self) -> NoReturn:
    -> 1577         raise ValueError(
       1578             f"The truth value of a {type(self).__name__} is ambiguous. "
       1579             "Use a.empty, a.bool(), a.item(), a.any() or a.all()."
       1580         )


    ValueError: The truth value of a Series is ambiguous. Use a.empty, a.bool(), a.item(), a.any() or a.all().



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