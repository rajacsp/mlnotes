---
title: Array-Sample
date: 2025-05-17
author: Your Name
cell_count: 3
score: 0
---

```python

```


```python
import numpy as np

a = np.array([1, 2, 3])  # Create a rank 1 array

print (type(a))            # Prints "<type 'numpy.ndarray'>"
print (a.shape)           # Prints "(3,)"
print (a[0], a[1], a[2])   # Prints "1 2 3"
a[0] = 5                 # Change an element of the array
print (a)                  # Prints "[5, 2, 3]"

b = np.array([[1,2,3],[4,5,6]])   # Create a rank 2 array
print (b.shape)                     # Prints "(2, 3)"
print (b[0, 0], b[0, 1], b[1, 0])   # Prints "1 2 4"

# test comment
```

    <class 'numpy.ndarray'>
    (3,)
    1 2 3
    [5 2 3]
    (2, 3)
    1 2 4



```python

```


---
**Score: 0**