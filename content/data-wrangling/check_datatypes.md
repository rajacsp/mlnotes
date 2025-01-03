---
title: Check Datatypes
date: 2025-01-03
author: Your Name
cell_count: 8
score: 5
---

---
title: "Check Data Types"
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
df = pd.read_csv("/Users/rajacsp/datasets/sales_data_types.csv")
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
      <th>Customer Number</th>
      <th>Customer Name</th>
      <th>2016</th>
      <th>2017</th>
      <th>Percent Growth</th>
      <th>Jan Units</th>
      <th>Month</th>
      <th>Day</th>
      <th>Year</th>
      <th>Active</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>10002.0</td>
      <td>Quest Industries</td>
      <td>$125,000.00</td>
      <td>$162500.00</td>
      <td>30.00%</td>
      <td>500</td>
      <td>1</td>
      <td>10</td>
      <td>2015</td>
      <td>Y</td>
    </tr>
    <tr>
      <th>1</th>
      <td>552278.0</td>
      <td>Smith Plumbing</td>
      <td>$920,000.00</td>
      <td>$101,2000.00</td>
      <td>10.00%</td>
      <td>700</td>
      <td>6</td>
      <td>15</td>
      <td>2014</td>
      <td>Y</td>
    </tr>
    <tr>
      <th>2</th>
      <td>23477.0</td>
      <td>ACME Industrial</td>
      <td>$50,000.00</td>
      <td>$62500.00</td>
      <td>25.00%</td>
      <td>125</td>
      <td>3</td>
      <td>29</td>
      <td>2016</td>
      <td>Y</td>
    </tr>
    <tr>
      <th>3</th>
      <td>24900.0</td>
      <td>Brekke LTD</td>
      <td>$350,000.00</td>
      <td>$490000.00</td>
      <td>4.00%</td>
      <td>75</td>
      <td>10</td>
      <td>27</td>
      <td>2015</td>
      <td>Y</td>
    </tr>
    <tr>
      <th>4</th>
      <td>651029.0</td>
      <td>Harbor Co</td>
      <td>$15,000.00</td>
      <td>$12750.00</td>
      <td>-15.00%</td>
      <td>Closed</td>
      <td>2</td>
      <td>2</td>
      <td>2014</td>
      <td>N</td>
    </tr>
  </tbody>
</table>
</div>




```python
df.dtypes
```




    Customer Number    float64
    Customer Name       object
    2016                object
    2017                object
    Percent Growth      object
    Jan Units           object
    Month                int64
    Day                  int64
    Year                 int64
    Active              object
    dtype: object




```python
df['Customer Number'].astype('int')
```




    0     10002
    1    552278
    2     23477
    3     24900
    4    651029
    Name: Customer Number, dtype: int64




```python
df.dtypes
```




    Customer Number    float64
    Customer Name       object
    2016                object
    2017                object
    Percent Growth      object
    Jan Units           object
    Month                int64
    Day                  int64
    Year                 int64
    Active              object
    dtype: object




```python

```


---
**Score: 5**