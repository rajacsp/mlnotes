---
title: Magicattr-Sample
date: 2024-12-06
author: Your Name
cell_count: 6
score: 5
---

---
title: "Magic Attribute Sample"
author: "Rj"
date: 2019-04-20
description: "-"
type: technical_note
draft: false
---

```python
import magicattr
```


```python
class City:
        
    def __init__(self, name, country):
        self.name = name
        self.country = country
```


```python
to = City('Toronto', 'Canada')
ch = City('Chennai', 'India')
```


```python
print(to)
```

    <__main__.City object at 0x10f2f8be0>



```python
print(magicattr.get(to, 'country'))
```

    Canada



---
**Score: 5**