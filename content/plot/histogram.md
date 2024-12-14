---
title: Histogram
date: 2024-12-14
author: Your Name
cell_count: 6
score: 5
---

---
title: "Histogram"
author: "Rj"
date: 2019-05-06
description: "List Test"
type: technical_note
draft: false
---

```python
import numpy as np
import matplotlib.pyplot as plt
```


```python
np.random.seed(13)
arr_data = np.random.normal(0,1, 100)
```


```python
yhist, binedges = np.histogram(arr_data)
```


```python
bincenters = np.mean(np.vstack([binedges[0:-1],binedges[1:]]), axis=0)
plt.bar(bincenters, yhist)
```




    <BarContainer object of 10 artists>




    
![png](/mlnotes/images/histogram_4_1.png)
    



```python

```


---
**Score: 5**