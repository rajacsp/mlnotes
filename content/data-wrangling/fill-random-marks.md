---
title: Fill-Random-Marks
date: 2024-12-26
author: Your Name
cell_count: 12
score: 10
---

---
title: "Fill Random Marks"
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
datatype = [('Science', 'int32'), ('Maths', 'int32')]
```


```python
current_values = np.zeros(3, dtype=datatype)
```


```python
current_index = ['Row '+str(i) for i in range(1, 4)]
```


```python
df = pd.DataFrame(current_values, index=current_index)
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
      <th>Science</th>
      <th>Maths</th>
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
df['Science']
```




    Row 1    0
    Row 2    0
    Row 3    0
    Name: Science, dtype: int32




```python
df['Science'][0] = 45
```


```python
df['Maths'][1] = 100
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
      <th>Science</th>
      <th>Maths</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Row 1</th>
      <td>45</td>
      <td>0</td>
    </tr>
    <tr>
      <th>Row 2</th>
      <td>0</td>
      <td>100</td>
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




---
**Score: 10**