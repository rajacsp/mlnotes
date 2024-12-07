---
title: Random-Int-With-2-Dim
date: 2024-12-07
author: Your Name
cell_count: 8
score: 5
---

---
title: "Random Integer with 2 dimension"
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
# Create Random integer between 1 to 100

df = pd.DataFrame(np.random.randint(0, 100, size=(2, 4)), columns=['A', 'B', 'C', 'D'])
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
      <th>A</th>
      <th>B</th>
      <th>C</th>
      <th>D</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>8</td>
      <td>45</td>
      <td>53</td>
      <td>45</td>
    </tr>
    <tr>
      <th>1</th>
      <td>14</td>
      <td>91</td>
      <td>77</td>
      <td>31</td>
    </tr>
  </tbody>
</table>
</div>




```python
df.shape
```




    (2, 4)




```python
df.describe()
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
      <th>A</th>
      <th>B</th>
      <th>C</th>
      <th>D</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>count</th>
      <td>2.000000</td>
      <td>2.000000</td>
      <td>2.000000</td>
      <td>2.000000</td>
    </tr>
    <tr>
      <th>mean</th>
      <td>11.000000</td>
      <td>68.000000</td>
      <td>65.000000</td>
      <td>38.000000</td>
    </tr>
    <tr>
      <th>std</th>
      <td>4.242641</td>
      <td>32.526912</td>
      <td>16.970563</td>
      <td>9.899495</td>
    </tr>
    <tr>
      <th>min</th>
      <td>8.000000</td>
      <td>45.000000</td>
      <td>53.000000</td>
      <td>31.000000</td>
    </tr>
    <tr>
      <th>25%</th>
      <td>9.500000</td>
      <td>56.500000</td>
      <td>59.000000</td>
      <td>34.500000</td>
    </tr>
    <tr>
      <th>50%</th>
      <td>11.000000</td>
      <td>68.000000</td>
      <td>65.000000</td>
      <td>38.000000</td>
    </tr>
    <tr>
      <th>75%</th>
      <td>12.500000</td>
      <td>79.500000</td>
      <td>71.000000</td>
      <td>41.500000</td>
    </tr>
    <tr>
      <th>max</th>
      <td>14.000000</td>
      <td>91.000000</td>
      <td>77.000000</td>
      <td>45.000000</td>
    </tr>
  </tbody>
</table>
</div>




```python
df.ndim
```




    2




```python

```


---
**Score: 5**