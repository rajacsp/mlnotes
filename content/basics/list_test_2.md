---
title: List Test 2
date: 2024-12-26
author: Your Name
cell_count: 10
score: 10
---

---
title: "List Test 2"
author: "Rj"
date: 2019-04-20
description: "List Test"
type: technical_note
draft: false
---

```python
entries = ['one', 2, 'three', False]
```


```python
print(entries)
```

    ['one', 2, 'three', False]



```python
print(entries[2:7])
```

    ['three', False]



```python
entryTuple = (100, 200, 'three', 'four')
print(entryTuple)
```

    (100, 200, 'three', 'four')



```python
cities = ['Toronto', 'Monteal', 'Vancouver']
print(cities)
```

    ['Toronto', 'Monteal', 'Vancouver']



```python
users = [
    ('Anders', 'A', 21),
    ('Balmer', 'B', 45),
    ('Stephe', 'S', 24)
]

print(users)
```

    [('Anders', 'A', 21), ('Balmer', 'B', 45), ('Stephe', 'S', 24)]



```python
sorted(users, key = lambda x: x[2])
```




    [('Anders', 'A', 21), ('Stephe', 'S', 24), ('Balmer', 'B', 45)]




```python
sorted(users, key = lambda x: -x[2])
```




    [('Balmer', 'B', 45), ('Stephe', 'S', 24), ('Anders', 'A', 21)]




```python

```


---
**Score: 10**