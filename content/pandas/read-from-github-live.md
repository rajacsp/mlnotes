---
title: Read-From-Github-Live
date: 2024-12-14
author: Your Name
cell_count: 11
score: 10
---

```python
# https://raw.githubusercontent.com/rajacsp/public-dataset/master/zynicide-wine-reviews/winemag-data-130k-v2.csv
```


```python
# https://github.com/rajacsp/public-dataset
```


```python
import requests
import pandas as pd
from io import BytesIO
```


```python
FILEPATH = 'https://raw.githubusercontent.com/rajacsp/public-dataset/master/zynicide-wine-reviews/winemag-data-130k-v2.csv'
```


```python
response = requests.get(FILEPATH)
```


```python
data = response.content
```


```python

```


```python
onlinedata = BytesIO(data)
```


```python
df = pd.read_csv(onlinedata, index_col=0)
```


```python
df.head(2)
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
      <th>country</th>
      <th>description</th>
      <th>designation</th>
      <th>points</th>
      <th>price</th>
      <th>province</th>
      <th>region_1</th>
      <th>region_2</th>
      <th>taster_name</th>
      <th>taster_twitter_handle</th>
      <th>title</th>
      <th>variety</th>
      <th>winery</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Italy</td>
      <td>Aromas include tropical fruit, broom, brimston...</td>
      <td>Vulkà Bianco</td>
      <td>87</td>
      <td>NaN</td>
      <td>Sicily &amp; Sardinia</td>
      <td>Etna</td>
      <td>NaN</td>
      <td>Kerin O’Keefe</td>
      <td>@kerinokeefe</td>
      <td>Nicosia 2013 Vulkà Bianco  (Etna)</td>
      <td>White Blend</td>
      <td>Nicosia</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Portugal</td>
      <td>This is ripe and fruity, a wine that is smooth...</td>
      <td>Avidagos</td>
      <td>87</td>
      <td>15.0</td>
      <td>Douro</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>Roger Voss</td>
      <td>@vossroger</td>
      <td>Quinta dos Avidagos 2011 Avidagos Red (Douro)</td>
      <td>Portuguese Red</td>
      <td>Quinta dos Avidagos</td>
    </tr>
  </tbody>
</table>
</div>




```python

```


---
**Score: 10**