---
title: Basic-Plot-1
date: 2025-01-04
author: Your Name
cell_count: 8
score: 5
---

---
title: "Basic Plot With Multiple Axes"
author: "Rj"
date: 2019-05-06
description: "List Test"
type: technical_note
draft: false
---

```python
import matplotlib.pyplot as plt
```


```python
x = [1, 2, 3, 4]
```


```python
y = [1, 4, 9, 16]
```


```python
z = [1, 8, 27, 64]
```


```python
x, y, z
```




    ([1, 2, 3, 4], [1, 4, 9, 16], [1, 8, 27, 64])




```python
plt.plot(x, y, z)
plt.axis([0, 10, 0, 80])
```




    [0, 10, 0, 80]




    
![png](/mlnotes/images/basic-plot-1_6_1.png)
    



```python

```


---
**Score: 5**