---
title: Chainmap
date: 2024-11-24
author: Your Name
cell_count: 17
score: 15
---

```python

```


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

```


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

    a ==> 2
    b ==> 3
    c ==> 4
    name ==> Toronto
    short_name ==> TO



```python
ab_list = list(ChainMap(city, number))
```


```python
ab_list
```




    ['a', 'b', 'c', 'name', 'short_name']




```python
ab_tuple = tuple(ChainMap(city, number))
```


```python
ab_tuple
```




    ('a', 'b', 'c', 'name', 'short_name')



Ref:

https://stackoverflow.com/questions/23392976/what-is-the-purpose-of-collections-chainmap

https://docs.python.org/3/library/collections.html#collections.Counter


```python

```


---
**Score: 15**