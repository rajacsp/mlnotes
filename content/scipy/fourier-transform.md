---
title: Fourier-Transform
date: 2024-12-14
author: Your Name
cell_count: 8
score: 5
---

---
title: "Fourier Transform"
author: "Raja CSP Raman"
date: 2019-05-06
description: "-"
type: technical_note
draft: false
---

```python
from scipy.fftpack import fft
import numpy as np
```


```python
x = np.array([1, 2, 3, 4])
```


```python
x
```




    array([1, 2, 3, 4])




```python
y = fft(x)
```


```python
y
```




    array([10.+0.j, -2.+2.j, -2.+0.j, -2.-2.j])




```python
import matplotlib.pyplot as plt
```


```python
plt.plot(x, y, 'ro')
plt.axis([-5, 20, -5, 20])
plt.show()
```

    /Users/rajacsp/anaconda3/envs/py36/lib/python3.6/site-packages/numpy/core/numeric.py:538: ComplexWarning: Casting complex values to real discards the imaginary part
      return array(a, dtype, copy=False, order=order)



    
![png](/mlnotes/images/fourier-transform_7_1.png)
    



---
**Score: 5**