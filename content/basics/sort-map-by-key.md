---
title: Sort-Map-By-Key
date: 2024-12-07
author: Your Name
cell_count: 7
score: 5
---

---
title: "Sort Map By Key"
author: "Rj"
date: 2019-04-20
description: "List Test"
type: technical_note
draft: false
---

```python
print('Hello Toronto')
```

    Hello Toronto



```python
def sort_by_key(dict):
    '''
        ::getRemotrAddr
    '''
    '''
    for key, value in sorted(dict.iteritems(), key=lambda(k,v): (v,k)):
        print("%s: %s" % (key, value))
    '''
    
    for key in sorted(dict.keys()):
        print("%s: %s" % (key, dict[key]))
    
    return None
```


```python
age = {
        'carl':40,
        'alan':2,
        'bob':1,
        'danny':3
    }
```


```python
age
```




    {'alan': 2, 'bob': 1, 'carl': 40, 'danny': 3}




```python
sort_by_key(age)
```

    alan: 2
    bob: 1
    carl: 40
    danny: 3



```python

```


---
**Score: 5**