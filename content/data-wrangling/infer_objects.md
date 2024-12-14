---
title: Infer Objects
date: 2024-12-14
author: Your Name
cell_count: 8
score: 5
---

---
title: "Infer Objects"
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
df = df.infer_objects()
```


```python
df.dtypes
```




    a     int64
    b    object
    dtype: object




```python
# You can see that dataype of column a is changed to int64.
```


---
**Score: 5**