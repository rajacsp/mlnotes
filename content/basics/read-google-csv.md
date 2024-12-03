---
title: Read-Google-Csv
date: 2024-12-03
author: Your Name
cell_count: 7
score: 5
---

---
title: "Read Google CSV"
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
filename = 'https://docs.google.com/spreadsheet/ccc?key=1EfyD7A4YcdAzTfUO0t3yQ0HawetVF5pefS5pPyGVX4g&output=csv'

r = requests.get(filename)
data = r.content
```


```python
df = pd.read_csv(BytesIO(data), index_col=0)
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
      <th>Song Name</th>
      <th>Language</th>
      <th>YouTube link</th>
      <th>Genre</th>
      <th>Artist</th>
      <th>Emotion Tag</th>
      <th>Emotion</th>
      <th>Hint</th>
      <th>Geo Location</th>
      <th>Lyrics</th>
      <th>Collector</th>
    </tr>
    <tr>
      <th>S. NO</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>1.0</th>
      <td>Classified - Inner</td>
      <td>English</td>
      <td>https://www.youtube.com/watch?v=NGhyL8zg3_I</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>Gives me some kind of confidence; Relaxed Cana...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>Raja</td>
    </tr>
    <tr>
      <th>2.0</th>
      <td>Avicii - Wake Me Up</td>
      <td>English</td>
      <td>https://www.youtube.com/watch?v=IcrbM1l_BoI</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>Raja</td>
    </tr>
    <tr>
      <th>3.0</th>
      <td>Ziroq - Que Pena</td>
      <td>NaN</td>
      <td>https://www.youtube.com/watch?v=Ws_5XC1qqpo</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>Raja</td>
    </tr>
    <tr>
      <th>4.0</th>
      <td>Koko show</td>
      <td>Finnish</td>
      <td>https://www.youtube.com/watch?v=pmbWpPztg8Y</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>Raja</td>
    </tr>
    <tr>
      <th>5.0</th>
      <td>Daniel Powter</td>
      <td>English</td>
      <td>https://www.youtube.com/watch?v=gH476CxJxfg</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>Raja</td>
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