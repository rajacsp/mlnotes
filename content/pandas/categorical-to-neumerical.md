---
title: Categorical-To-Neumerical
date: 2024-11-21
author: Your Name
cell_count: 8
score: 5
---

```python
import numpy as np
import pandas as pd
```


```python
data = {
    'sam' : ['archery', 'badminton', 'athletics', 'cycling_road', 'canoe_sprint', 'boxing'],
    'medal' : ['gold', 'silver', 'bronze', 'gold', 'gold', 'silver']
}
```


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
      <th>sam</th>
      <th>medal</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>archery</td>
      <td>gold</td>
    </tr>
    <tr>
      <th>1</th>
      <td>badminton</td>
      <td>silver</td>
    </tr>
    <tr>
      <th>2</th>
      <td>athletics</td>
      <td>bronze</td>
    </tr>
    <tr>
      <th>3</th>
      <td>cycling_road</td>
      <td>gold</td>
    </tr>
    <tr>
      <th>4</th>
      <td>canoe_sprint</td>
      <td>gold</td>
    </tr>
    <tr>
      <th>5</th>
      <td>boxing</td>
      <td>silver</td>
    </tr>
  </tbody>
</table>
</div>




```python
def get_medal_points(medal):
    if(medal == 'gold'):
        return 10
    
    if(medal == 'silver'):
        return 5
    
    if(medal == 'bronze'):
        return 1
    
    return 0
```


```python
df['medal_points'] = df['medal'].apply(get_medal_points)
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
      <th>sam</th>
      <th>medal</th>
      <th>medal_points</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>archery</td>
      <td>gold</td>
      <td>10</td>
    </tr>
    <tr>
      <th>1</th>
      <td>badminton</td>
      <td>silver</td>
      <td>5</td>
    </tr>
    <tr>
      <th>2</th>
      <td>athletics</td>
      <td>bronze</td>
      <td>1</td>
    </tr>
    <tr>
      <th>3</th>
      <td>cycling_road</td>
      <td>gold</td>
      <td>10</td>
    </tr>
    <tr>
      <th>4</th>
      <td>canoe_sprint</td>
      <td>gold</td>
      <td>10</td>
    </tr>
    <tr>
      <th>5</th>
      <td>boxing</td>
      <td>silver</td>
      <td>5</td>
    </tr>
  </tbody>
</table>
</div>




```python

```


---
**Score: 5**