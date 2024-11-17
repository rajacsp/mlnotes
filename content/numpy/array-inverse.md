---
title: Array-Inverse
date: 2024-11-17
author: Your Name
cell_count: 6
score: 5
---

```python
import numpy as np
```


```python
a = np.array([
    [1, 2],
    [3, 4]
])
```


```python
a
```




    array([[1, 2],
           [3, 4]])




```python
inverse_a = np.linalg.inv(a)
```


```python
print(inverse_a)
```

    [[-2.   1. ]
     [ 1.5 -0.5]]



```python

```


---
**Score: 5**
