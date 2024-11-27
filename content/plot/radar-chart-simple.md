---
title: Radar-Chart-Simple
date: 2024-11-27
author: Your Name
cell_count: 9
score: 5
---

---
title: "Radar Chart Simple"
author: "Rj"
date: 2019-04-20
description: "List Test"
type: technical_note
draft: false
---

```python
import matplotlib.pyplot as plt
import pandas as pd
from math import pi
```


```python
df = pd.DataFrame({
    'group' : ['A', 'B', 'C', 'D'],
    
    'var1' : [10, 20, 30, 4],
    'var2' : [2, 88, 22, 2]
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
      <th>group</th>
      <th>var1</th>
      <th>var2</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>A</td>
      <td>10</td>
      <td>2</td>
    </tr>
    <tr>
      <th>1</th>
      <td>B</td>
      <td>20</td>
      <td>88</td>
    </tr>
    <tr>
      <th>2</th>
      <td>C</td>
      <td>30</td>
      <td>22</td>
    </tr>
    <tr>
      <th>3</th>
      <td>D</td>
      <td>4</td>
      <td>2</td>
    </tr>
  </tbody>
</table>
</div>




```python
# number of variable
categories = list(df)[1:]
N = len(categories)
```


```python
# Assign values
values = df.loc[0].drop('group').values.flatten().tolist()
values += values[:1]
values
```




    [10, 2, 10]




```python
angles = [n / float(N) * 2* pi for n in range(N)]
angles += angles[:1]
```


```python
angles
```




    [0.0, 3.141592653589793, 0.0]




```python
# Initiliaze Spider plot
ax = plt.subplot(111, polar=True)

plt.xticks(angles[:-1], categories, color='grey', size=8)

ax.set_rlabel_position(0)
plt.yticks([10, 20, 30], ["10", "20", "39"], color="grey", size=7)
plt.ylim(0, 40)


# Plot data
ax.plot(angles, values, linewidth=1, linestyle='solid')

ax.fill(angles, values, 'b', alpha=0.1)
```




    [<matplotlib.patches.Polygon at 0x119d7f710>]




    
![png](/mlnotes/images/radar-chart-simple_8_1.png)
    



---
**Score: 5**