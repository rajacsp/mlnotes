---
title: Basic-Plot
date: 2024-12-07
author: Your Name
cell_count: 6
score: 5
---

---
title: "Basic Plot"
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
y = [2, 4, 9, 16]
```


```python
x, y
```




    ([1, 2, 3, 4], [2, 4, 9, 16])




```python
plt.plot(x, y, 'ro')
plt.axis([0, 10, 0, 20])
```




    [0, 10, 0, 20]




    
![png](/mlnotes/images/basic-plot_5_1.png)
    



---
**Score: 5**