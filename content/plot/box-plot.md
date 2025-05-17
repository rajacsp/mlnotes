---
title: Box-Plot
date: 2025-05-17
author: Your Name
cell_count: 10
score: 10
---

---
title: "Box Plot"
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
    [19, 11, 8]
])
```


```python
abc
```




    array([[ 9, 13, 10],
           [ 7, 12,  9],
           [19, 11,  8]])




```python
df2 = pd.DataFrame(abc, columns=['breakfast', 'lunch', 'dinner'])
```


```python
df2.plot.bar()
```




    <matplotlib.axes._subplots.AxesSubplot at 0x114cacf28>




    
![png](/mlnotes/images/box-plot_5_1.png)
    



```python
df2.plot.barh()
```




    <matplotlib.axes._subplots.AxesSubplot at 0x114aa1278>




    
![png](/mlnotes/images/box-plot_6_1.png)
    



```python
df2.plot.barh(stacked=True)
```




    <matplotlib.axes._subplots.AxesSubplot at 0x114caccc0>




    
![png](/mlnotes/images/box-plot_7_1.png)
    



```python

```


```python

```


---
**Score: 10**