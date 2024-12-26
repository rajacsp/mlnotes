---
title: Apply Function-2933
date: 2024-12-26
author: Your Name
cell_count: 9
score: 5
---

---
title: "Apply Function"
author: "Rj"
date: 2019-04-20
description: "List Test"
type: technical_note
draft: false
---

```python
import pandas as pd
```


```python
data = {
    'city' : ['Toronto', 'Montreal', 'Waterloo', 'Toronto', 'Waterloo', 'Toronto', 'Toronto'],
    'points' : [80, 70, 90, 85, 79, 82, 200]
}
```


```python
data
```




    {'city': ['Toronto',
      'Montreal',
      'Waterloo',
      'Toronto',
      'Waterloo',
      'Toronto',
      'Toronto'],
     'points': [80, 70, 90, 85, 79, 82, 200]}




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
    <tr>
      <th>3</th>
      <td>Toronto</td>
      <td>85</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Waterloo</td>
      <td>79</td>
    </tr>
    <tr>
      <th>5</th>
      <td>Toronto</td>
      <td>82</td>
    </tr>
    <tr>
      <th>6</th>
      <td>Toronto</td>
      <td>200</td>
    </tr>
  </tbody>
</table>
</div>




```python
df.groupby('city')['points'].apply(lambda x:x.rolling(window=1).mean())
```




    0     80.0
    1     70.0
    2     90.0
    3     85.0
    4     79.0
    5     82.0
    6    200.0
    Name: points, dtype: float64




```python
df.groupby('city')['points'].apply(lambda x:x.rolling(window=2).mean())
```




    0      NaN
    1      NaN
    2      NaN
    3     82.5
    4     84.5
    5     83.5
    6    141.0
    Name: points, dtype: float64




---
**Score: 5**