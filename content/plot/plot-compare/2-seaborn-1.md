---
title: 2-Seaborn-1
date: 2024-12-06
author: Your Name
cell_count: 6
score: 5
---

```python
import pyutil as pyu
```


```python
pyu.get_local_pyinfo()
```




    'conda env: ml312-2024; pyv: 3.12.7 | packaged by Anaconda, Inc. | (main, Oct  4 2024, 13:27:36) [GCC 11.2.0]'




```python

```


```python
!pip show seaborn | grep "Version:"
```

    Version: 0.13.2



```python
import seaborn as sns
import pandas as pd

data = pd.DataFrame({'x': [1, 2, 3, 4], 'y': [10, 20, 25, 30]})
sns.lineplot(data=data, x='x', y='y')

```




    <Axes: xlabel='x', ylabel='y'>




    
![png](/mlnotes/images/2-seaborn-1_4_1.png)
    



```python

```


---
**Score: 5**