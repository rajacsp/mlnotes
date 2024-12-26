---
title: Random-Plot-Simple
date: 2024-12-26
author: Your Name
cell_count: 7
score: 5
---

---
title: "Random Plot Simple"
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
df = pd.DataFrame(np.random.randn(100, 4), index=pd.date_range('1/1/2000', periods=100), columns=list('ABCD'))
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
      <td>-0.996724</td>
      <td>-0.378036</td>
      <td>0.779475</td>
      <td>0.903508</td>
    </tr>
    <tr>
      <th>2000-01-02</th>
      <td>-0.571293</td>
      <td>-0.348798</td>
      <td>1.272404</td>
      <td>-0.262368</td>
    </tr>
    <tr>
      <th>2000-01-03</th>
      <td>0.673788</td>
      <td>-0.895174</td>
      <td>-0.078577</td>
      <td>-0.371040</td>
    </tr>
    <tr>
      <th>2000-01-04</th>
      <td>-1.792242</td>
      <td>1.015611</td>
      <td>-0.267689</td>
      <td>-0.241193</td>
    </tr>
    <tr>
      <th>2000-01-05</th>
      <td>-0.081370</td>
      <td>0.230835</td>
      <td>0.135019</td>
      <td>0.321915</td>
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




    <matplotlib.axes._subplots.AxesSubplot at 0x108be9c88>




    
![png](/mlnotes/images/random-plot-simple_5_1.png)
    



```python

```


---
**Score: 5**