---
title: Random-Number-Plot
date: 2024-12-25
author: Your Name
cell_count: 5
score: 5
---

---
title: "Random Number Plot"
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
a = np.random.randint(10, size=20)
```


```python
a
```




    array([2, 5, 5, 4, 9, 0, 4, 9, 0, 1, 9, 7, 9, 7, 1, 5, 7, 0, 8, 2])




```python
plt.plot(a, np.sin(a))
plt.show()
```


    
![png](/mlnotes/images/random-number-plot_4_0.png)
    



---
**Score: 5**