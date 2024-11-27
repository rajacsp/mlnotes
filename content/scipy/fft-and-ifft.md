---
title: Fft-And-Ifft
date: 2024-11-27
author: Your Name
cell_count: 9
score: 5
---

---
title: "FFT and IFFT"
author: "Raja CSP Raman"
date: 2019-05-06
description: "-"
type: technical_note
draft: false
---

```python
from scipy.fftpack import fft, ifft
import numpy as np
```


```python
x = np.array([1, 2, 4, 5])
```


```python
x
```




    array([1, 2, 4, 5])




```python
y = fft(x)
```


```python
y
```




    array([12.+0.j, -3.+3.j, -2.+0.j, -3.-3.j])




```python
y_inv = ifft(y)
```


```python
y_inv
```




    array([1.+0.j, 2.+0.j, 4.+0.j, 5.+0.j])




```python

```


---
**Score: 5**