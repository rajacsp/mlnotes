---
title: Iloc
date: 2024-11-24
author: Your Name
cell_count: 5
score: 5
---

---
title: "iLoc Simple"
author: "Rj"
date: 2019-04-20
description: "-"
type: technical_note
draft: false
---

```python
import pandas as pd
```


```python
df = pd.read_csv('data1.csv', sep=',', header=None)
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
      <th>0</th>
      <th>1</th>
      <th>2</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>capacity</td>
      <td>score</td>
      <td>length</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1</td>
      <td>10</td>
      <td>30</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2</td>
      <td>20</td>
      <td>30</td>
    </tr>
    <tr>
      <th>3</th>
      <td>3</td>
      <td>30</td>
      <td>40</td>
    </tr>
    <tr>
      <th>4</th>
      <td>3</td>
      <td>40</td>
      <td>30</td>
    </tr>
    <tr>
      <th>5</th>
      <td>2</td>
      <td>30</td>
      <td>40</td>
    </tr>
    <tr>
      <th>6</th>
      <td>7</td>
      <td>10</td>
      <td>23</td>
    </tr>
    <tr>
      <th>7</th>
      <td>3</td>
      <td>20</td>
      <td>22</td>
    </tr>
    <tr>
      <th>8</th>
      <td>8</td>
      <td>20</td>
      <td>11</td>
    </tr>
    <tr>
      <th>9</th>
      <td>2</td>
      <td>30</td>
      <td>2</td>
    </tr>
  </tbody>
</table>
</div>




```python
print(df.iloc[:4]) # 0 - 4 = 5 values
```

              0      1       2
    0  capacity  score  length
    1         1     10      30
    2         2     20      30
    3         3     30      40



---
**Score: 5**