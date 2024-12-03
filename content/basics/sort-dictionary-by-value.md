---
title: Sort-Dictionary-By-Value
date: 2024-12-03
author: Your Name
cell_count: 13
score: 10
---

---
title: "Sort Dictionary By Value"
author: "Rj"
date: 2019-04-20
description: "List Test"
type: technical_note
draft: false
---

```python
dict = {
    'one' : 8,
    'two' : 1,
    'three' : 12
}
```


```python
dict
```




    {'one': 8, 'three': 12, 'two': 1}




```python
import operator


sorted_x = sorted(dict.items(), key=operator.itemgetter(1))
```


```python
sorted_x
```




    [('two', 1), ('one', 8), ('three', 12)]




```python
type(sorted_x)
```




    list




```python
import collections
```


```python
sorted_dict = collections.OrderedDict(dict)
```


```python
sorted_dict
```




    OrderedDict([('one', 8), ('two', 1), ('three', 12)])




```python
# Reverse sort

reverse_dict= sorted(dict.items(), key=lambda x: x[1], reverse=True)
```


```python
reverse_dict
```




    [('three', 12), ('one', 8), ('two', 1)]




```python
for x in reverse_dict:
    print(x[0], "==>", x[1])
```

    three ==> 12
    one ==> 8
    two ==> 1



```python

```


---
**Score: 10**