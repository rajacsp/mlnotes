---
title: Gruopby Date
date: 2025-01-03
author: Your Name
cell_count: 10
score: 10
---

---
title: "Groupby Date"
author: "Rj"
date: 2019-04-20
description: "List Test"
type: technical_note
draft: false
---

```python
from datetime import datetime
import pandas as pd
```


```python
data = {
    'date' : [
        '2019-05-01 19:47:05.069722', 
        '2019-05-02 17:47:05.069722', 
        '2019-05-02 19:47:05.069722',
        '2019-05-03 18:47:05.069722',
        '2019-05-03 19:47:05.069722',
    ],
    'spent' : [
        13, 
        13,
        11,
        15,
        10
    ]  
}
```


```python
data
```




    {'date': ['2019-05-01 19:47:05.069722',
      '2019-05-02 17:47:05.069722',
      '2019-05-02 19:47:05.069722',
      '2019-05-03 18:47:05.069722',
      '2019-05-03 19:47:05.069722'],
     'spent': [13, 13, 11, 15, 10]}




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
      <th>date</th>
      <th>spent</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>2019-05-01 19:47:05.069722</td>
      <td>13</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2019-05-02 17:47:05.069722</td>
      <td>13</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2019-05-02 19:47:05.069722</td>
      <td>11</td>
    </tr>
    <tr>
      <th>3</th>
      <td>2019-05-03 18:47:05.069722</td>
      <td>15</td>
    </tr>
    <tr>
      <th>4</th>
      <td>2019-05-03 19:47:05.069722</td>
      <td>10</td>
    </tr>
  </tbody>
</table>
</div>




```python
# Convert to String date teo datetime and then to date
df['date'] = pd.to_datetime(df['date']).dt.date
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
      <th>date</th>
      <th>spent</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>2019-05-01</td>
      <td>13</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2019-05-02</td>
      <td>13</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2019-05-02</td>
      <td>11</td>
    </tr>
    <tr>
      <th>3</th>
      <td>2019-05-03</td>
      <td>15</td>
    </tr>
    <tr>
      <th>4</th>
      <td>2019-05-03</td>
      <td>10</td>
    </tr>
  </tbody>
</table>
</div>




```python
df.groupby('date').mean()
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
      <th>spent</th>
    </tr>
    <tr>
      <th>date</th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2019-05-01</th>
      <td>13.0</td>
    </tr>
    <tr>
      <th>2019-05-02</th>
      <td>12.0</td>
    </tr>
    <tr>
      <th>2019-05-03</th>
      <td>12.5</td>
    </tr>
  </tbody>
</table>
</div>




```python
# If you want to get only integers, use as type (or .round(0) since 0.17.0)
df.groupby('date').mean().astype(int) 
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
      <th>spent</th>
    </tr>
    <tr>
      <th>date</th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2019-05-01</th>
      <td>13</td>
    </tr>
    <tr>
      <th>2019-05-02</th>
      <td>12</td>
    </tr>
    <tr>
      <th>2019-05-03</th>
      <td>12</td>
    </tr>
  </tbody>
</table>
</div>




---
**Score: 10**