---
title: Reduce-Advanced
date: 2025-01-03
author: Your Name
cell_count: 8
score: 5
---

---
title: "Reduce Advanced"
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
def do_magic(a, b): 
    
    if((a % 2 == 1) & (b % 2 == 1) ):
        return a * b
    
    return a + b
```


```python
do_magic(10, 15)
```




    25




```python
do_magic(11, 15)
```




    165




```python
reduce(do_magic, [10, 20, 30, 40])
```




    100




```python
reduce(do_magic, [10, 20, 30, 40, 31, 41])
```




    5371




```python

```


---
**Score: 5**