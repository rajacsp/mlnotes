---
title: Yahoo-Data-2
date: 2025-01-04
author: Your Name
cell_count: 8
score: 5
---

```python

```


```python
import pyutil as pyu
pyu.get_local_pyinfo()
```




    'conda env: ml312-2024; pyv: 3.12.7 | packaged by Anaconda, Inc. | (main, Oct  4 2024, 13:27:36) [GCC 11.2.0]'




```python
# !pip install yfinance --upgrade --no-cache-dir
```


```python
print(pyu.ps2("pandas yfinance"))
```

    pandas==2.2.3
    yfinance==0.2.51
    



```python

```


```python
import yfinance as yf
from datetime import datetime

# Define the start and end dates
start = datetime(1976, 1, 1)
end = datetime(2013, 12, 31)

# Download data using yfinance
sp = yf.download('^GSPC', start=start, end=end)

print(sp.head())  # Display the first few rows of data
```

    [*********************100%***********************]  1 of 1 completed

    Price           Close       High        Low  Open    Volume
    Ticker          ^GSPC      ^GSPC      ^GSPC ^GSPC     ^GSPC
    Date                                                       
    1976-01-02  90.900002  91.180000  89.809998   0.0  10300000
    1976-01-05  92.580002  92.839996  90.849998   0.0  21960000
    1976-01-06  93.529999  94.180000  92.370003   0.0  31270000
    1976-01-07  93.949997  95.150002  92.910004   0.0  33170000
    1976-01-08  94.580002  95.470001  93.410004   0.0  29030000


    



```python

```


```python

```


---
**Score: 5**