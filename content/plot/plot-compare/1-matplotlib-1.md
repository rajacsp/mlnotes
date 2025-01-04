---
title: 1-Matplotlib-1
date: 2025-01-04
author: Your Name
cell_count: 6
score: 5
---

```python
import pyutil as pyu
pyu.get_local_pyinfo()
```




    'conda env: ml312-2024; pyv: 3.12.7 | packaged by Anaconda, Inc. | (main, Oct  4 2024, 13:27:36) [GCC 11.2.0]'




```python

```




    'conda env: ml312-2024; pyv: 3.12.7 | packaged by Anaconda, Inc. | (main, Oct  4 2024, 13:27:36) [GCC 11.2.0]'




```python

```


```python
!pip show matplotlib | grep "Version:"
```

    Version: 3.9.3



```python
import matplotlib.pyplot as plt

x = [1, 2, 3, 4]
y = [10, 20, 25, 30]
plt.plot(x, y, label='Line 1')
plt.title("Simple Plot")
plt.legend()
plt.show()
```


    
![png](/mlnotes/images/1-matplotlib-1_4_0.png)
    



```python

```


---
**Score: 5**