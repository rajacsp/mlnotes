---
title: Itertool Chain
date: 2024-12-14
author: Your Name
cell_count: 9
score: 5
---

---
title: "Itertool Chain"
author: "Rj"
date: 2019-04-20
description: "List Test"
type: technical_note
draft: false
---

```python
from itertools import chain
```


```python
string = 'Toronto'
chain(string)
```




    <itertools.chain at 0x108ed2ba8>




```python
chars = chain(string)
```


```python
type(chars)
```




    itertools.chain




```python
chars
```




    <itertools.chain at 0x108ed2b70>




```python
for c in chars:
    print(c)
```

    T
    o
    r
    o
    n
    t
    o



```python
for c in chars:
    print(c)
```


```python
# Since the iteration is finished, you can't get the characters one more time
```


---
**Score: 5**