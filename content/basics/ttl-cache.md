---
title: Ttl-Cache
date: 2024-12-05
author: Your Name
cell_count: 8
score: 5
---

---
title: "TTL Cache"
author: "Rj"
date: 2019-04-20
description: "-"
type: technical_note
draft: false
---

```python
from cachetools import TTLCache
```


```python
cache = TTLCache(maxsize=10, ttl=10)
```


```python
cache['city'] = 'Toronto'
```


```python
cache['city']
```




    'Toronto'




```python
# Run the cell below after 10 seconds
```


```python
cache['city']
```




    'Toronto'




```python
# more 
# https://stackoverflow.com/questions/31771286/python-in-memory-cache-with-time-to-live
```


---
**Score: 5**