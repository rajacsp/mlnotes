---
title: Reducer
date: 2025-05-17
author: Your Name
cell_count: 8
score: 5
---

---
title: "Reducers"
author: "Rj"
date: 2019-04-20
description: "-"
type: technical_note
draft: false
---

```python
import functools as fnt
```


```python
list = [10, 40, 20, 50, 30, 90]
```


```python
list
```




    [10, 40, 20, 50, 30, 90]




```python
sum_list = fnt.reduce(lambda x, y: x+y, list)
```


```python
sum_list
```




    240




```python
def get_sum(list):
    return fnt.reduce(lambda x,y : x+y, list)
```


```python
print(get_sum(list))
```

    240



---
**Score: 5**