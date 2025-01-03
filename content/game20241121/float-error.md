---
title: Float-Error
date: 2025-01-03
author: Your Name
cell_count: 2
score: 0
---

```python
try:
    "soemthing".toFloat
except (ValueError, KeyError, AttributeError) as e:
    print('error : ', str(e))
    print(getattr(e, 'message', repr(e)))
```

    error :  'str' object has no attribute 'toFloat'
    AttributeError("'str' object has no attribute 'toFloat'")



```python

```


---
**Score: 0**