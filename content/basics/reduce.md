---
title: Reduce
date: 2025-01-04
author: Your Name
cell_count: 6
score: 5
---

---
title: "Reduce"
author: "Rj"
date: 2019-04-20
description: "List Test"
type: technical_note
draft: false
---

```python
from functools import reduce
```


```python
def add(a, b): 
    return a + b
```


```python
add(10, 15)
```




    25




```python
reduce(add, [10, 20, 30, 40])
```




    100




```python

```


---
**Score: 5**