---
title: Read-Google-Csv-With-Date
date: 2025-01-04
author: Your Name
cell_count: 7
score: 5
---

---
title: "Read Google CSV with Date"
author: "Raja CSP Raman"
date: 2019-04-20
description: "-"
type: technical_note
draft: false
---

```python
from io import BytesIO
import requests
import pandas as pd
```


```python
filename = 'https://docs.google.com/spreadsheet/ccc?key=0Ak1ecr7i0wotdGJmTURJRnZLYlV3M2daNTRubTdwTXc&output=csv'

r = requests.get(filename)
data = r.content
```


```python
df = pd.read_csv(BytesIO(data), index_col=0,parse_dates=['Quradate'])
```


```python
df.head()
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
      <th>City</th>
      <th>region</th>
      <th>Res_Comm</th>
      <th>mkt_type</th>
      <th>Quradate</th>
      <th>National_exp</th>
      <th>Alabama_exp</th>
      <th>Sales_exp</th>
      <th>Inventory_exp</th>
      <th>Price_exp</th>
      <th>Credit_exp</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Dothan</td>
      <td>South_Central-Montgomery-Auburn-Wiregrass-Dothan</td>
      <td>Residential</td>
      <td>Rural</td>
      <td>2010-01-15</td>
      <td>2</td>
      <td>2</td>
      <td>3</td>
      <td>2</td>
      <td>3</td>
      <td>3</td>
    </tr>
    <tr>
      <th>10</th>
      <td>Foley</td>
      <td>South_Mobile-Baldwin</td>
      <td>Residential</td>
      <td>Suburban_Urban</td>
      <td>2010-01-15</td>
      <td>4</td>
      <td>4</td>
      <td>4</td>
      <td>4</td>
      <td>4</td>
      <td>3</td>
    </tr>
    <tr>
      <th>12</th>
      <td>Birmingham</td>
      <td>North_Central-Birmingham-Tuscaloosa-Anniston</td>
      <td>Commercial</td>
      <td>Suburban_Urban</td>
      <td>2010-01-15</td>
      <td>2</td>
      <td>2</td>
      <td>3</td>
      <td>2</td>
      <td>2</td>
      <td>3</td>
    </tr>
    <tr>
      <th>38</th>
      <td>Brent</td>
      <td>North_Central-Birmingham-Tuscaloosa-Anniston</td>
      <td>Residential</td>
      <td>Rural</td>
      <td>2010-01-15</td>
      <td>3</td>
      <td>3</td>
      <td>3</td>
      <td>3</td>
      <td>3</td>
      <td>2</td>
    </tr>
    <tr>
      <th>44</th>
      <td>Athens</td>
      <td>North_Huntsville-Decatur-Florence</td>
      <td>Residential</td>
      <td>Suburban_Urban</td>
      <td>2010-01-15</td>
      <td>4</td>
      <td>5</td>
      <td>4</td>
      <td>4</td>
      <td>4</td>
      <td>4</td>
    </tr>
  </tbody>
</table>
</div>




```python
# source : https://stackoverflow.com/questions/19611729/getting-google-spreadsheet-csv-into-a-pandas-dataframe
```


```python

```


---
**Score: 5**