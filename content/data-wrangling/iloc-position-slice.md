---
title: Iloc-Position-Slice
date: 2024-12-07
author: Your Name
cell_count: 8
score: 5
---

---
title: "iLoc Position Slice"
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
df = pd.read_csv('data1.csv')
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
      <th>capacity</th>
      <th>score</th>
      <th>length</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>10</td>
      <td>30</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2</td>
      <td>20</td>
      <td>30</td>
    </tr>
    <tr>
      <th>2</th>
      <td>3</td>
      <td>30</td>
      <td>40</td>
    </tr>
    <tr>
      <th>3</th>
      <td>3</td>
      <td>40</td>
      <td>30</td>
    </tr>
    <tr>
      <th>4</th>
      <td>2</td>
      <td>30</td>
      <td>40</td>
    </tr>
    <tr>
      <th>5</th>
      <td>7</td>
      <td>10</td>
      <td>23</td>
    </tr>
    <tr>
      <th>6</th>
      <td>3</td>
      <td>20</td>
      <td>22</td>
    </tr>
    <tr>
      <th>7</th>
      <td>8</td>
      <td>20</td>
      <td>11</td>
    </tr>
    <tr>
      <th>8</th>
      <td>2</td>
      <td>30</td>
      <td>2</td>
    </tr>
  </tbody>
</table>
</div>




```python
df.iloc[2:8]
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
      <th>capacity</th>
      <th>score</th>
      <th>length</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2</th>
      <td>3</td>
      <td>30</td>
      <td>40</td>
    </tr>
    <tr>
      <th>3</th>
      <td>3</td>
      <td>40</td>
      <td>30</td>
    </tr>
    <tr>
      <th>4</th>
      <td>2</td>
      <td>30</td>
      <td>40</td>
    </tr>
    <tr>
      <th>5</th>
      <td>7</td>
      <td>10</td>
      <td>23</td>
    </tr>
    <tr>
      <th>6</th>
      <td>3</td>
      <td>20</td>
      <td>22</td>
    </tr>
    <tr>
      <th>7</th>
      <td>8</td>
      <td>20</td>
      <td>11</td>
    </tr>
  </tbody>
</table>
</div>




```python
df.iloc[8]
```




    capacity     2
    score       30
    length       2
    Name: 8, dtype: int64




```python
df.iloc[7]
```




    capacity     8
    score       20
    length      11
    Name: 7, dtype: int64




```python

```


---
**Score: 5**