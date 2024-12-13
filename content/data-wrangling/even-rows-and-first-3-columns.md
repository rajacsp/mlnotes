---
title: Even-Rows-And-First-3-Columns
date: 2024-12-13
author: Your Name
cell_count: 8
score: 5
---

---
title: "Even Rows and 3 Columns"
author: "Rj"
date: 2019-04-22
description: "-"
type: technical_note
draft: false
---

```python
import numpy as np
import pandas as pd
```


```python
df = pd.read_csv('abc.csv', sep=',', encoding='utf-8')
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
      <th>student</th>
      <th>language</th>
      <th>science</th>
      <th>maths</th>
      <th>history</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>kumar</td>
      <td>90</td>
      <td>56</td>
      <td>34</td>
      <td>34</td>
    </tr>
    <tr>
      <th>1</th>
      <td>kevin</td>
      <td>10</td>
      <td>34</td>
      <td>32</td>
      <td>67</td>
    </tr>
    <tr>
      <th>2</th>
      <td>sammy</td>
      <td>90</td>
      <td>23</td>
      <td>12</td>
      <td>32</td>
    </tr>
    <tr>
      <th>3</th>
      <td>janice</td>
      <td>20</td>
      <td>67</td>
      <td>90</td>
      <td>45</td>
    </tr>
    <tr>
      <th>4</th>
      <td>peter</td>
      <td>30</td>
      <td>56</td>
      <td>45</td>
      <td>65</td>
    </tr>
    <tr>
      <th>5</th>
      <td>prem</td>
      <td>90</td>
      <td>45</td>
      <td>45</td>
      <td>34</td>
    </tr>
    <tr>
      <th>6</th>
      <td>carrol</td>
      <td>50</td>
      <td>90</td>
      <td>45</td>
      <td>23</td>
    </tr>
  </tbody>
</table>
</div>




```python
df_even = df[::2]
```


```python
df_even
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
      <th>student</th>
      <th>language</th>
      <th>science</th>
      <th>maths</th>
      <th>history</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>kumar</td>
      <td>90</td>
      <td>56</td>
      <td>34</td>
      <td>34</td>
    </tr>
    <tr>
      <th>2</th>
      <td>sammy</td>
      <td>90</td>
      <td>23</td>
      <td>12</td>
      <td>32</td>
    </tr>
    <tr>
      <th>4</th>
      <td>peter</td>
      <td>30</td>
      <td>56</td>
      <td>45</td>
      <td>65</td>
    </tr>
    <tr>
      <th>6</th>
      <td>carrol</td>
      <td>50</td>
      <td>90</td>
      <td>45</td>
      <td>23</td>
    </tr>
  </tbody>
</table>
</div>




```python
# Even rows and first 3 columns

df_even_3 = df.iloc[::2, :3]
```


```python
df_even_3
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
      <th>student</th>
      <th>language</th>
      <th>science</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>kumar</td>
      <td>90</td>
      <td>56</td>
    </tr>
    <tr>
      <th>2</th>
      <td>sammy</td>
      <td>90</td>
      <td>23</td>
    </tr>
    <tr>
      <th>4</th>
      <td>peter</td>
      <td>30</td>
      <td>56</td>
    </tr>
    <tr>
      <th>6</th>
      <td>carrol</td>
      <td>50</td>
      <td>90</td>
    </tr>
  </tbody>
</table>
</div>




---
**Score: 5**