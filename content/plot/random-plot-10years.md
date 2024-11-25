---
title: Random-Plot-10Years
date: 2024-11-25
author: Your Name
cell_count: 8
score: 5
---

---
title: "Random Plot 10 years"
author: "Rj"
date: 2019-05-06
description: "List Test"
type: technical_note
draft: false
---

```python
import numpy as np
import pandas as pd
```


```python
df = pd.DataFrame(np.random.randn(4000, 4), index=pd.date_range('1/1/2000', periods=4000), columns=list('ABCD'))
```


```python
df.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>A</th>
      <th>B</th>
      <th>C</th>
      <th>D</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2000-01-01</th>
      <td>-1.784755</td>
      <td>-0.673046</td>
      <td>1.126506</td>
      <td>-0.306832</td>
    </tr>
    <tr>
      <th>2000-01-02</th>
      <td>-2.915124</td>
      <td>-1.512690</td>
      <td>-0.116375</td>
      <td>2.526247</td>
    </tr>
    <tr>
      <th>2000-01-03</th>
      <td>1.486783</td>
      <td>-0.827375</td>
      <td>0.510406</td>
      <td>-0.406183</td>
    </tr>
    <tr>
      <th>2000-01-04</th>
      <td>-1.288162</td>
      <td>-1.455968</td>
      <td>-0.212177</td>
      <td>-0.474076</td>
    </tr>
    <tr>
      <th>2000-01-05</th>
      <td>-0.787701</td>
      <td>-0.048756</td>
      <td>-1.552077</td>
      <td>-2.018627</td>
    </tr>
  </tbody>
</table>
</div>




```python
df = df.cumsum()
```


```python
df.plot()
```




    <matplotlib.axes._subplots.AxesSubplot at 0x113eb0710>




    
![png](/mlnotes/images/random-plot-10years_5_1.png)
    



```python

```


```python

```


---
**Score: 5**