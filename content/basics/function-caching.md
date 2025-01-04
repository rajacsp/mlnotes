---
title: Function-Caching
date: 2025-01-04
author: Your Name
cell_count: 11
score: 10
---

---
title: "Function Caching"
author: "Rj"
date: 2019-04-20
description: "-"
type: technical_note
draft: false
---

```python
from functools import lru_cache
```


```python
@lru_cache(maxsize=10)
def add(a, b):
    print('add method called')
    return a+b
```


```python
print(add(7, 4))
```

    add method called
    11



```python
print(add(7, 4))
```

    11



```python
print(add(5, 2))
```

    add method called
    7



```python
print(add(5, 2))
```

    7



```python
# clear cache
add.cache_clear()
```


```python
print(add(5, 2))
```

    add method called
    7



```python
print(add(5, 2))
```

    7



```python

```


---
**Score: 10**