---
title: String-To-Dataframe
date: 2024-12-07
author: Your Name
cell_count: 8
score: 5
---

---
title: "String to Dataframe"
author: "Rj"
date: 2019-04-22
description: "-"
type: technical_note
draft: false
---

```python
import numpy as np
import pandas as pd
from io import StringIO
```


```python
content = """
    1, 2
    3, 4
    5, 6
"""
```


```python
content
```




    '\n    1, 2\n    3, 4\n    5, 6\n'




```python
df = pd.read_csv(StringIO(content), header=None)
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
      <th>0</th>
      <th>1</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>2</td>
    </tr>
    <tr>
      <th>1</th>
      <td>3</td>
      <td>4</td>
    </tr>
    <tr>
      <th>2</th>
      <td>5</td>
      <td>6</td>
    </tr>
  </tbody>
</table>
</div>




```python
df.shape
```




    (3, 2)




```python
df.describe()
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
      <th>0</th>
      <th>1</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>count</th>
      <td>3.0</td>
      <td>3.0</td>
    </tr>
    <tr>
      <th>mean</th>
      <td>3.0</td>
      <td>4.0</td>
    </tr>
    <tr>
      <th>std</th>
      <td>2.0</td>
      <td>2.0</td>
    </tr>
    <tr>
      <th>min</th>
      <td>1.0</td>
      <td>2.0</td>
    </tr>
    <tr>
      <th>25%</th>
      <td>2.0</td>
      <td>3.0</td>
    </tr>
    <tr>
      <th>50%</th>
      <td>3.0</td>
      <td>4.0</td>
    </tr>
    <tr>
      <th>75%</th>
      <td>4.0</td>
      <td>5.0</td>
    </tr>
    <tr>
      <th>max</th>
      <td>5.0</td>
      <td>6.0</td>
    </tr>
  </tbody>
</table>
</div>




---
**Score: 5**