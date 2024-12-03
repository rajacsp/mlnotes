---
title: Copy List
date: 2024-12-03
author: Your Name
cell_count: 11
score: 10
---

---
title: "Copy List"
author: "Rj"
date: 2019-04-20
description: "List Test"
type: technical_note
draft: false
---

```python
import copy
```


```python
a = [1, 2, 3]
```


```python
b = copy.copy(a)
```


```python
b
```




    [1, 2, 3]




```python
b.append(4)
```


```python
a
```




    [1, 2, 3]




```python
b
```




    [1, 2, 3, 4]




```python
# deep copy

c = copy.deepcopy(a)
```


```python
c
```




    [1, 2, 3]



More:
    
    https://stackoverflow.com/questions/2612802/how-to-clone-or-copy-a-list


---
**Score: 10**