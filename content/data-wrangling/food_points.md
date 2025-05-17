---
title: Food Points
date: 2025-05-17
author: Your Name
cell_count: 9
score: 5
---

---
title: "Food Points"
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
data = {
    'dinner' : ['chicken wrap', 'stake', 'rudy burger', 'sushi', 'chicken teriyaki', 'caesar salad']
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
      <th>dinner</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>chicken wrap</td>
    </tr>
    <tr>
      <th>1</th>
      <td>stake</td>
    </tr>
    <tr>
      <th>2</th>
      <td>rudy burger</td>
    </tr>
    <tr>
      <th>3</th>
      <td>sushi</td>
    </tr>
    <tr>
      <th>4</th>
      <td>chicken teriyaki</td>
    </tr>
    <tr>
      <th>5</th>
      <td>caesar salad</td>
    </tr>
  </tbody>
</table>
</div>




```python
def get_food_points(food):
    if('chicken' in food):
        return 2
    
    if('stake' in food):
        return 1
    
    if('burger' in food):
        return 1

    if('salad' in food):
        return 7
    
    return None
```


```python
df['food_points'] = df['dinner'].apply(get_food_points)
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
      <th>dinner</th>
      <th>food_points</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>chicken wrap</td>
      <td>2.0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>stake</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>rudy burger</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>3</th>
      <td>sushi</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>4</th>
      <td>chicken teriyaki</td>
      <td>2.0</td>
    </tr>
    <tr>
      <th>5</th>
      <td>caesar salad</td>
      <td>7.0</td>
    </tr>
  </tbody>
</table>
</div>




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
      <th>dinner</th>
      <th>food_points</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>chicken wrap</td>
      <td>2.0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>stake</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>rudy burger</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>3</th>
      <td>sushi</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>4</th>
      <td>chicken teriyaki</td>
      <td>2.0</td>
    </tr>
    <tr>
      <th>5</th>
      <td>caesar salad</td>
      <td>7.0</td>
    </tr>
  </tbody>
</table>
</div>




---
**Score: 5**