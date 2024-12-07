---
title: Loc With Boolean
date: 2024-12-07
author: Your Name
cell_count: 7
score: 5
---

---
title: "If Else Pandas"
author: "Rj"
date: 2019-04-24
description: "-"
type: technical_note
draft: false
source: http://pandas.pydata.org/pandas-docs/version/0.24/user_guide/cookbook.html#idioms
---

```python
import numpy as np
import pandas as pd
```


```python
df = pd.DataFrame({
    'maths' : [80, 89, 90, 20],
    'science' : [40, 50, 90, 100],
    'language' : [20, 30, 90, 95]
})
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
      <th>maths</th>
      <th>science</th>
      <th>language</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>80</td>
      <td>40</td>
      <td>20</td>
    </tr>
    <tr>
      <th>1</th>
      <td>89</td>
      <td>50</td>
      <td>30</td>
    </tr>
    <tr>
      <th>2</th>
      <td>90</td>
      <td>90</td>
      <td>90</td>
    </tr>
    <tr>
      <th>3</th>
      <td>20</td>
      <td>100</td>
      <td>95</td>
    </tr>
  </tbody>
</table>
</div>




```python
df.loc[df.maths > 50, 'maths_1'] = 90
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
      <th>maths</th>
      <th>science</th>
      <th>language</th>
      <th>maths_1</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>80</td>
      <td>40</td>
      <td>20</td>
      <td>90.0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>89</td>
      <td>50</td>
      <td>30</td>
      <td>90.0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>90</td>
      <td>90</td>
      <td>90</td>
      <td>90.0</td>
    </tr>
    <tr>
      <th>3</th>
      <td>20</td>
      <td>100</td>
      <td>95</td>
      <td>NaN</td>
    </tr>
  </tbody>
</table>
</div>




```python

```


---
**Score: 5**