---
title: Static-On-The-Fly
date: 2024-11-27
author: Your Name
cell_count: 5
score: 5
---

---
title: "Static on the fly"
author: "Rj"
date: 2019-04-20
description: "-"
type: technical_note
draft: false
---

```python
class Mathematics:

    def addNumbers(x, y):
        return x + y
```


```python
# create addNumbers static method
Mathematics.addNumbers = staticmethod(Mathematics.addNumbers)
```


```python
print('The sum is:', Mathematics.addNumbers(5, 10))
```

    The sum is: 15



```python

```


---
**Score: 5**