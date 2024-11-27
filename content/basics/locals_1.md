---
title: Locals 1
date: 2024-11-27
author: Your Name
cell_count: 5
score: 5
---

---
title: "Locals of Function"
author: "Rj"
date: 2019-04-20
description: "List Test"
type: technical_note
draft: false
---

```python
def myFunc():
    print("hello")
```


```python
fname = "myFunc"
```


```python
f = locals()[fname]
f()
```

    hello



```python
f = eval(fname)
f()
```

    hello



---
**Score: 5**