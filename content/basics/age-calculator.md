---
title: Age-Calculator
date: 2024-11-16
author: Your Name
cell_count: 5
score: 5
---

```python
from datetime import datetime
```


```python
def get_age(d):
    d1 = datetime.now()
    months = (d1.year - d.year) * 12 + d1.month - d.month

    year = int(months / 12)
    return year
```


```python
age = get_age(datetime(1991, 1, 1))
```


```python
age
```




    33




```python

```


---
**Score: 5**
