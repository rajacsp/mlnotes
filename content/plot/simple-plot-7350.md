---
title: Simple-Plot-7350
date: 2024-12-07
author: Your Name
cell_count: 4
score: 0
---

---
title: "Simple Plot"
author: "Rj"
date: 2019-04-20
description: "List Test"
type: technical_note
draft: false
---

```python
import matplotlib.pyplot as plt
import numpy as np
```


```python
N = 128
x = np.linspace(-5, 5, N)
y = np.exp(-x**2)

y_fft = np.fft.fftshift(np.fft.fft(y).real)
plt.plot(x, y_fft)

plt.show()
```


    
![png](/mlnotes/images/simple-plot_2_0.png)
    



```python

```


---
**Score: 0**