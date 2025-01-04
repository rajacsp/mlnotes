---
title: Food-Plot
date: 2025-01-04
author: Your Name
cell_count: 8
score: 5
---

---
title: "Food Plot"
author: "Rj"
date: 2019-05-06
description: "List Test"
type: technical_note
draft: false
---

```python
import pandas as pd
import numpy as np
```


```python
abc = np.array([
    [9, 13, 10],
    [7, 12, 9],
    [19, 11, 8],
    [12, 10, 11]
])
```


```python
abc
```




    array([[ 9, 13, 10],
           [ 7, 12,  9],
           [19, 11,  8],
           [12, 10, 11]])




```python
df2 = pd.DataFrame(abc, columns=['breakfast', 'lunch', 'dinner'])
```


```python
df2.plot()
```




    <matplotlib.axes._subplots.AxesSubplot at 0x122961780>




    
![png](/mlnotes/images/food-plot_5_1.png)
    



```python

```


```python

```


---
**Score: 5**