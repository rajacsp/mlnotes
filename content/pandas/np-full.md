---
title: Np-Full
date: 2025-05-17
author: Your Name
cell_count: 10
score: 10
---

```python

```


```python
import pyutil as pyu
pyu.get_local_pyinfo()
```




    'conda env: ml312-2024; pyv: 3.12.7 | packaged by Anaconda, Inc. | (main, Oct  4 2024, 13:27:36) [GCC 11.2.0]'




```python
print(pyu.ps2("pandas"))
```

    pandas==2.2.3
    



```python

```


```python
from functools import reduce
product = reduce((lambda x, y: x * y), [1, 2, 3, 4])
```


```python
product
```




    24




```python

```


```python
import numpy as np
```


```python
sizes = np.full((10), 7, dtype=int)
sizes
```




    array([7, 7, 7, 7, 7, 7, 7, 7, 7, 7])




```python

```


---
**Score: 10**