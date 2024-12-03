---
title: Fibonacci-Generator
date: 2024-12-04
author: Your Name
cell_count: 5
score: 5
---

---
title: "Fibonacci in Generator"
author: "Rj"
date: 2019-04-20
description: "-"
type: technical_note
draft: false
---

```python
def fibonacci(n):
    a = b = 1
    
    for i in range(n):
        yield a
        a, b = b, a+b
```


```python
print(2)
```

    2



```python
for x in fibonacci(10):
    print(x)
```

    1
    1
    2
    3
    5
    8
    13
    21
    34
    55



```python

```


---
**Score: 5**