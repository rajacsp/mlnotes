---
title: Timeit-Simple-2
date: 2024-12-03
author: Your Name
cell_count: 5
score: 5
---

---
title: "Timeit Simple 2"
author: "Rj"
date: 2019-04-20
description: "-"
type: technical_note
draft: false
---

```python
import timeit
```


```python
def some_function():
    return map(lambda x: x^2, range(10))
```


```python
time1 = timeit.timeit(some_function)
print(time1)
```

    0.39235781200113706



```python
print(time1)
```

    0.39235781200113706



---
**Score: 5**