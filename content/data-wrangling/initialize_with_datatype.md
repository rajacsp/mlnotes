---
title: Initialize With Datatype
date: 2024-12-14
author: Your Name
cell_count: 10
score: 10
---

---
title: "Initalize With DataType"
author: "Rj"
date: 2019-04-24
description: "-"
type: technical_note
draft: false
---

```python
import numpy as np
import pandas as pd
```


```python
df = pd.DataFrame({'a': [7, 1, 5], 'b': ['3','2','1']}, dtype='object')
```


```python
df
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
      <th>a</th>
      <th>b</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>7</td>
      <td>3</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1</td>
      <td>2</td>
    </tr>
    <tr>
      <th>2</th>
      <td>5</td>
      <td>1</td>
    </tr>
  </tbody>
</table>
</div>




```python
df.dtypes
```




    a    object
    b    object
    dtype: object




```python
# Let's set the datatype as integer
df1 = pd.DataFrame({'a': [7, 1, 5], 'b': ['3','2','1']}, dtype='int')
```

    /Users/rajacsp/anaconda3/envs/py36/lib/python3.6/site-packages/numpy/core/numeric.py:2591: FutureWarning: elementwise comparison failed; returning scalar instead, but in the future will perform elementwise comparison
      return bool(asarray(a1 == a2).all())



```python
df1
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
      <th>a</th>
      <th>b</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>7</td>
      <td>3</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1</td>
      <td>2</td>
    </tr>
    <tr>
      <th>2</th>
      <td>5</td>
      <td>1</td>
    </tr>
  </tbody>
</table>
</div>




```python
type(df1)
```




    pandas.core.frame.DataFrame




```python
df1.dtypes
```




    a    int64
    b    int64
    dtype: object




```python

```


---
**Score: 10**