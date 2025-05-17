---
title: Yahoo-Data-3
date: 2025-05-17
author: Your Name
cell_count: 6
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
print(pyu.ps2("pandas"))
```

    pandas==2.2.3
    



```python

```


```python
import yfinance as yf
import pandas as pd
from datetime import datetime

# Define the start and end dates
start = "1976-01-01"
end = "2013-12-31"

# Download S&P 500 data using yfinance
sp = yf.download('^GSPC', start=start, end=end)

sp.head()
```

    [*********************100%***********************]  1 of 1 completed





<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead tr th {
        text-align: left;
    }

    .dataframe thead tr:last-of-type th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr>
      <th>Price</th>
      <th>Close</th>
      <th>High</th>
      <th>Low</th>
      <th>Open</th>
      <th>Volume</th>
    </tr>
    <tr>
      <th>Ticker</th>
      <th>^GSPC</th>
      <th>^GSPC</th>
      <th>^GSPC</th>
      <th>^GSPC</th>
      <th>^GSPC</th>
    </tr>
    <tr>
      <th>Date</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>1976-01-02</th>
      <td>90.900002</td>
      <td>91.180000</td>
      <td>89.809998</td>
      <td>0.0</td>
      <td>10300000</td>
    </tr>
    <tr>
      <th>1976-01-05</th>
      <td>92.580002</td>
      <td>92.839996</td>
      <td>90.849998</td>
      <td>0.0</td>
      <td>21960000</td>
    </tr>
    <tr>
      <th>1976-01-06</th>
      <td>93.529999</td>
      <td>94.180000</td>
      <td>92.370003</td>
      <td>0.0</td>
      <td>31270000</td>
    </tr>
    <tr>
      <th>1976-01-07</th>
      <td>93.949997</td>
      <td>95.150002</td>
      <td>92.910004</td>
      <td>0.0</td>
      <td>33170000</td>
    </tr>
    <tr>
      <th>1976-01-08</th>
      <td>94.580002</td>
      <td>95.470001</td>
      <td>93.410004</td>
      <td>0.0</td>
      <td>29030000</td>
    </tr>
  </tbody>
</table>
</div>




```python

```


---
**Score: 5**