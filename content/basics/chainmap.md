---
title: Chainmap
date: 2025-01-04
author: Your Name
cell_count: 15
score: 15
---

---
title: "Chainmap"
author: "Rj"
date: 2019-04-20
description: "List Test"
type: technical_note
draft: false
---

```python
city = {'name': 'Toronto', 'short_name': 'TO'}
```


```python
number = {'a': 2, 'b': 3, 'c' : 4}
```


```python
city
```




    {'name': 'Toronto', 'short_name': 'TO'}




```python
number
```




    {'a': 2, 'b': 3, 'c': 4}




```python
from collections import ChainMap
```


```python
ab = ChainMap(city, number)
```


```python
ab
```




    ChainMap({'name': 'Toronto', 'short_name': 'TO'}, {'a': 2, 'b': 3, 'c': 4})




```python
type(ab)
```




    collections.ChainMap




```python
for k, v in ab.items():
    print(k , "==>", v)
```

    short_name ==> TO
    b ==> 3
    c ==> 4
    a ==> 2
    name ==> Toronto



```python
ab_list = list(ChainMap(city, number))
```


```python
ab_list
```




    ['short_name', 'b', 'c', 'a', 'name']




```python
ab_tuple = tuple(ChainMap(city, number))
```


```python
ab_tuple
```




    ('short_name', 'b', 'c', 'a', 'name')



more: 

https://stackoverflow.com/questions/23392976/what-is-the-purpose-of-collections-chainmap

https://docs.python.org/3/library/collections.html#collections.Counter


---
**Score: 15**