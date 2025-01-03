---
title: List Ref
date: 2025-01-03
author: Your Name
cell_count: 12
score: 10
---

---
title: "List Reference"
author: "Rj"
date: 2019-04-20
description: "List Test"
type: technical_note
draft: false
---

```python
a = [
    1, 2, 3, 4
]
```


```python
b = a
```


```python
b
```




    [1, 2, 3, 4]




```python
b.append(5)
```


```python
a
```




    [1, 2, 3, 4, 5]



As b is referring to a, whatever is added to b, will be reflected to a as well

If you don't want such behavior, just use .copy() or a[:]


```python
c = a.copy()
```


```python
c.append(6)
```


```python
a
```




    [1, 2, 3, 4, 5]






---
**Score: 10**