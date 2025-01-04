---
title: Pandas-With-Random-Int
date: 2025-01-04
author: Your Name
cell_count: 4
score: 0
---

---
title: "Pandas with Random Int"
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
df = pd.DataFrame(np.random.randint(0, 100, size=(3, 2)), columns=list('xy'))
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
      <th>x</th>
      <th>y</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>63</td>
      <td>81</td>
    </tr>
    <tr>
      <th>1</th>
      <td>54</td>
      <td>35</td>
    </tr>
    <tr>
      <th>2</th>
      <td>63</td>
      <td>67</td>
    </tr>
  </tbody>
</table>
</div>




---
**Score: 0**