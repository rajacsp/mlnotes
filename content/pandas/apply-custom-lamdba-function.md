---
title: Apply-Custom-Lamdba-Function
date: 2024-12-07
author: Your Name
cell_count: 11
score: 10
---

```python
import numpy as np
import pandas as pd
```


```python
data = {
    'city' : ['Toronto', 'Montreal', 'Waterloo'],
    'points' : [80, 70, 90]
}
```


```python
data
```




    {'city': ['Toronto', 'Montreal', 'Waterloo'], 'points': [80, 70, 90]}




```python
type(data)
```




    dict




```python
df = pd.DataFrame(data)
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
      <th>city</th>
      <th>points</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Toronto</td>
      <td>80</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Montreal</td>
      <td>70</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Waterloo</td>
      <td>90</td>
    </tr>
  </tbody>
</table>
</div>




```python
def get_bonus(x):
    if (x > 75):
        return x + 10
    return x
```


```python
df['new_points'] = df['points'].apply(lambda x: get_bonus(x))
```


```python
df['new_points']
```




    0     90
    1     70
    2    100
    Name: new_points, dtype: int64




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
      <th>city</th>
      <th>points</th>
      <th>new_points</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Toronto</td>
      <td>80</td>
      <td>90</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Montreal</td>
      <td>70</td>
      <td>70</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Waterloo</td>
      <td>90</td>
      <td>100</td>
    </tr>
  </tbody>
</table>
</div>




```python

```


---
**Score: 10**