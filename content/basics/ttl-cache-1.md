---
title: Ttl-Cache-1
date: 2024-12-14
author: Your Name
cell_count: 9
score: 5
---

---
title: "TTL Cache Check"
author: "Rj"
date: 2019-04-20
description: "-"
type: technical_note
draft: false
---

```python
from cachetools import TTLCache 
import time
```


```python
cache = TTLCache(maxsize=10, ttl=10)
```


```python
cache['city'] = 'Toronto'
```


```python
print(cache['city'])
```

    Toronto



```python
time.sleep(5)
```


```python
if('city' in cache):
    print(cache['city'])
else:
    print('Cache not found')
```

    Toronto



```python
time.sleep(5)
```


```python
print('city' in cache)
```

    False



---
**Score: 5**