---
title: Values-And-Index
date: 2024-11-24
author: Your Name
cell_count: 9
score: 5
---

---
title: "Values and Index"
author: "Rj"
date: 2019-04-22
description: "-"
type: technical_note
draft: false
---

```python
import numpy as np
import pandas as pd
```


```python
datatype = [('one', 'int32'), ('two', 'int32')]
```


```python
values = np.zeros(3, dtype = datatype)
```


```python
currrent_index = ['Row '+str(i) for i in range(1, 4)]
```


```python
df = pd.DataFrame(values, index = currrent_index)
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
      <th>one</th>
      <th>two</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Row 1</th>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>Row 2</th>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>Row 3</th>
      <td>0</td>
      <td>0</td>
    </tr>
  </tbody>
</table>
</div>




```python
df.shape
```




    (3, 2)




```python
df.ndim
```




    2




---
**Score: 5**