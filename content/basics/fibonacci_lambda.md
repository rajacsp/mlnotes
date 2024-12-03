---
title: Fibonacci Lambda
date: 2024-12-03
author: Your Name
cell_count: 5
score: 5
---

---
title: "Fibonacci Lambda"
author: "Rj"
date: 2019-04-20
description: "List Test"
type: technical_note
draft: false
---

```python
def print_fibo(number):
    print(list(map(lambda x, f = lambda x, f : (f(x-1,f) + f(x-2,f)) if x > 1 else 1: f(x,f), range(number))))
```


```python
print_fibo(6)
```

    [1, 1, 2, 3, 5, 8]



```python
print_fibo(16)
```

    [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987]



```python

```


---
**Score: 5**