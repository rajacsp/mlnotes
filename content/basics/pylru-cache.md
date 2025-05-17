---
title: Pylru-Cache
date: 2025-05-17
author: Your Name
cell_count: 15
score: 15
---

---
title: "Pylru Cache"
author: "Rj"
date: 2019-04-20
description: "-"
type: technical_note
draft: false
---

```python
import pylru
```


```python
cache = pylru.lrucache(100)
```


```python
cache
```




    <pylru.lrucache at 0x112997fd0>




```python
# add 
cache['name'] = 'One'
```


```python
cache['name']
```




    'One'




```python
# add 
cache['city'] = 'Toronto'
```


```python
'city' in cache # this doesn't affect the cache order
```




    True




```python
cache.keys()
```




    <generator object lrucache.keys at 0x1129923b8>




```python
for key in cache.keys():
    print(key)
```

    city
    name



```python
for value in cache.values():
    print(value)
```

    Toronto
    One



```python
for k, v in cache.items():
    print(k, v)
```

    city Toronto
    name One



```python
cache.clear()
```


```python
cache
```




    <pylru.lrucache at 0x112997fd0>




```python
'name' in cache
```




    False




---
**Score: 15**