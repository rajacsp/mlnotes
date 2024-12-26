---
title: Sin-Plot
date: 2024-12-26
author: Your Name
cell_count: 9
score: 5
---

---
title: "Sin Plot"
author: "Rj"
date: 2019-04-20
description: "List Test"
type: technical_note
draft: false
---

```python
import numpy as np
import matplotlib.pylab as plt
```


```python
x = np.arange(20, 29)
```


```python
print(x)
```

    [20 21 22 23 24 25 26 27 28]



```python
y = np.sin(x)
```


```python
print(y)
```

    [ 0.91294525  0.83665564 -0.00885131 -0.8462204  -0.90557836 -0.13235175
      0.76255845  0.95637593  0.27090579]



```python
plot = plt.plot(x, y)
plt.grid(True)
```


```python
plt.show()
```


    
![png](/mlnotes/images/sin-plot_7_0.png)
    



```python

```


---
**Score: 5**