---
title: Lambda-Odd
date: 2025-01-03
author: Your Name
cell_count: 7
score: 5
---

---
title: "Lambda Odd"
author: "Raja CSP Raman"
date: 2019-04-20
description: "-"
type: technical_note
draft: false
---

```python
def is_odd(digit):
    if digit % 2 != 0:
        return True
    
    return False 
```


```python
digits = [
    1, 7, 18, 2, 4, 2, 8, 5, 3
    ]
```


```python
digits
```




    [1, 7, 18, 2, 4, 2, 8, 5, 3]




```python
new_list = list(filter(lambda x: is_odd(x) , digits))
```


```python
new_list
```




    [1, 7, 5, 3]




```python

```


---
**Score: 5**