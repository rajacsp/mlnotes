---
title: 04-Parabolic-Sar-1
date: 2025-05-17
author: Your Name
cell_count: 11
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
# !pip install ta
```


```python
print(pyu.ps2("requests ta"))
```

    requests==2.32.3
    ta==0.11.0
    



```python

```


```python
import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
from ta.trend import PSARIndicator

# Step 1: Download historical data
symbol = "^GSPC"  # S&P 500 as an example
start = "2020-01-01"
end = "2023-12-31"
data = yf.download(symbol, start=start, end=end)

# Step 2: Handle missing data
data.dropna(inplace=True)  # Remove rows with missing values

# Step 3: Calculate Parabolic SAR
psar = PSARIndicator(high=data['High'], low=data['Low'], close=data['Close'], step=0.02, max_step=0.2)
data['PSAR'] = psar.psar()

# Step 4: Plot the data with Parabolic SAR
plt.figure(figsize=(14, 7))
plt.plot(data['Close'], label='Close Price', color='blue', linewidth=1)
plt.scatter(data.index, data['PSAR'], label='Parabolic SAR', color='red', marker='.', alpha=0.7)
plt.title(f'Parabolic SAR for {symbol}')
plt.xlabel('Date')
plt.ylabel('Price')
plt.legend(loc='best')
plt.grid(True)
plt.show()
```

    [*********************100%***********************]  1 of 1 completed



    ---------------------------------------------------------------------------

    ValueError                                Traceback (most recent call last)

    /tmp/ipykernel_866231/3893101634.py in ?()
         12 # Step 2: Handle missing data
         13 data.dropna(inplace=True)  # Remove rows with missing values
         14 
         15 # Step 3: Calculate Parabolic SAR
    ---> 16 psar = PSARIndicator(high=data['High'], low=data['Low'], close=data['Close'], step=0.02, max_step=0.2)
         17 data['PSAR'] = psar.psar()
         18 
         19 # Step 4: Plot the data with Parabolic SAR


    ~/miniconda3/envs/ml312-2024/lib/python3.12/site-packages/ta/trend.py in ?(self, high, low, close, step, max_step, fillna)
        965         self._close = close
        966         self._step = step
        967         self._max_step = max_step
        968         self._fillna = fillna
    --> 969         self._run()
    

    ~/miniconda3/envs/ml312-2024/lib/python3.12/site-packages/ta/trend.py in ?(self)
        988                 self._psar.iloc[i] = self._psar.iloc[i - 1] + (
        989                     acceleration_factor * (up_trend_high - self._psar.iloc[i - 1])
        990                 )
        991 
    --> 992                 if min_low < self._psar.iloc[i]:
        993                     reversal = True
        994                     self._psar.iloc[i] = up_trend_high
        995                     down_trend_low = min_low


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
import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

# Step 1: Download historical data
symbol = "^GSPC"  # S&P 500 as an example
start = "2020-01-01"
end = "2023-12-31"
data = yf.download(symbol, start=start, end=end)

# Step 2: Define a function to calculate Parabolic SAR
def calculate_psar(data, step=0.02, max_step=0.2):
    psar = data['Close'].copy()
    high = data['High']
    low = data['Low']
    
    # Initializing trend direction and parameters
    trend = 1  # 1 for uptrend, -1 for downtrend
    af = step  # Acceleration factor
    ep = high.iloc[0] if trend == 1 else low.iloc[0]  # Extreme point
    
    for i in range(1, len(data)):
        prev_psar = psar.iloc[i - 1]
        
        # Calculate the new SAR
        new_psar = prev_psar + af * (ep - prev_psar)
        
        # Update the extreme point and acceleration factor
        if trend == 1:  # Uptrend
            ep = max(ep, high.iloc[i])
            if low.iloc[i] < new_psar:
                trend = -1
                af = step
                ep = low.iloc[i]
                new_psar = high.iloc[i - 1]
        else:  # Downtrend
            ep = min(ep, low.iloc[i])
            if high.iloc[i] > new_psar:
                trend = 1
                af = step
                ep = high.iloc[i]
                new_psar = low.iloc[i - 1]
        
        # Prevent SAR from exceeding the previous period's high or low
        if trend == 1:
            new_psar = min(new_psar, low.iloc[i - 1])
        else:
            new_psar = max(new_psar, high.iloc[i - 1])
        
        # Update the SAR and AF
        psar.iloc[i] = new_psar
        af = min(af + step, max_step) if trend == 1 else af

    return psar

# Step 3: Apply the function
data['PSAR'] = calculate_psar(data)

# Step 4: Plot the data with Parabolic SAR
plt.figure(figsize=(14, 7))
plt.plot(data['Close'], label='Close Price', color='blue', linewidth=1)
plt.scatter(data.index, data['PSAR'], label='Parabolic SAR', color='red', marker='.', alpha=0.7)
plt.title(f'Parabolic SAR for {symbol}')
plt.xlabel('Date')
plt.ylabel('Price')
plt.legend(loc='best')
plt.grid(True)
plt.show()
```

    [*********************100%***********************]  1 of 1 completed



    ---------------------------------------------------------------------------

    ValueError                                Traceback (most recent call last)

    /tmp/ipykernel_866231/4205552620.py in ?()
         53 
         54     return psar
         55 
         56 # Step 3: Apply the function
    ---> 57 data['PSAR'] = calculate_psar(data)
         58 
         59 # Step 4: Plot the data with Parabolic SAR
         60 plt.figure(figsize=(14, 7))


    /tmp/ipykernel_866231/4205552620.py in ?(data, step, max_step)
         26         new_psar = prev_psar + af * (ep - prev_psar)
         27 
         28         # Update the extreme point and acceleration factor
         29         if trend == 1:  # Uptrend
    ---> 30             ep = max(ep, high.iloc[i])
         31             if low.iloc[i] < new_psar:
         32                 trend = -1
         33                 af = step


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
import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

# Step 1: Download historical data
symbol = "^GSPC"  # S&P 500 as an example
start = "2020-01-01"
end = "2023-12-31"
data = yf.download(symbol, start=start, end=end)

# Step 2: Define a function to calculate Parabolic SAR
def calculate_psar(data, step=0.02, max_step=0.2):
    high = data['High']
    low = data['Low']
    close = data['Close']
    
    psar = close.copy()  # Initialize the Parabolic SAR series
    trend = 1  # Start with an uptrend (1 for uptrend, -1 for downtrend)
    af = step  # Initial Acceleration Factor
    ep = high.iloc[0] if trend == 1 else low.iloc[0]  # Extreme Point

    for i in range(1, len(data)):
        # Calculate new PSAR value
        new_psar = psar.iloc[i - 1] + af * (ep - psar.iloc[i - 1])
        
        # Check for trend reversal
        if trend == 1:  # Uptrend
            if low.iloc[i] < new_psar:  # Trend reversal to downtrend
                trend = -1
                psar.iloc[i] = high.iloc[i - 1]
                ep = low.iloc[i]
                af = step
            else:
                ep = max(ep, high.iloc[i])
                psar.iloc[i] = new_psar
        else:  # Downtrend
            if high.iloc[i] > new_psar:  # Trend reversal to uptrend
                trend = 1
                psar.iloc[i] = low.iloc[i - 1]
                ep = high.iloc[i]
                af = step
            else:
                ep = min(ep, low.iloc[i])
                psar.iloc[i] = new_psar
        
        # Adjust the Acceleration Factor
        af = min(af + step, max_step) if trend == 1 else af

        # Prevent PSAR from exceeding the previous period's high or low
        if trend == 1:
            psar.iloc[i] = min(psar.iloc[i], low.iloc[i - 1])
        else:
            psar.iloc[i] = max(psar.iloc[i], high.iloc[i - 1])
    
    return psar

# Step 3: Apply the function
data['PSAR'] = calculate_psar(data)

# Step 4: Plot the data with Parabolic SAR
plt.figure(figsize=(14, 7))
plt.plot(data['Close'], label='Close Price', color='blue', linewidth=1)
plt.scatter(data.index, data['PSAR'], label='Parabolic SAR', color='red', marker='.', alpha=0.7)
plt.title(f'Parabolic SAR for {symbol}')
plt.xlabel('Date')
plt.ylabel('Price')
plt.legend(loc='best')
plt.grid(True)
plt.show()
```

    [*********************100%***********************]  1 of 1 completed



    ---------------------------------------------------------------------------

    ValueError                                Traceback (most recent call last)

    /tmp/ipykernel_866231/2848592418.py in ?()
         54 
         55     return psar
         56 
         57 # Step 3: Apply the function
    ---> 58 data['PSAR'] = calculate_psar(data)
         59 
         60 # Step 4: Plot the data with Parabolic SAR
         61 plt.figure(figsize=(14, 7))


    /tmp/ipykernel_866231/2848592418.py in ?(data, step, max_step)
         24         new_psar = psar.iloc[i - 1] + af * (ep - psar.iloc[i - 1])
         25 
         26         # Check for trend reversal
         27         if trend == 1:  # Uptrend
    ---> 28             if low.iloc[i] < new_psar:  # Trend reversal to downtrend
         29                 trend = -1
         30                 psar.iloc[i] = high.iloc[i - 1]
         31                 ep = low.iloc[i]


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


---
**Score: 10**