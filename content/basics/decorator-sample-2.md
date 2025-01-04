---
title: Decorator-Sample-2
date: 2025-01-04
author: Your Name
cell_count: 6
score: 5
---

---
title: "Decorator Sample 2"
author: "Rj"
date: 2019-04-20
description: "-"
type: technical_note
draft: false
---

```python
class my_decorator(object):

    def __init__(self, f):
        print("inside my_decorator.__init__()")
        f() # Prove that function definition has completed

    def __call__(self):
        print("inside my_decorator.__call__()")
```


```python
@my_decorator
def aFunction():
    print("inside aFunction()")
```

    inside my_decorator.__init__()
    inside aFunction()



```python
print("Finished decorating aFunction()")
```

    Finished decorating aFunction()



```python
aFunction()
```

    inside my_decorator.__call__()



```python

```


---
**Score: 5**