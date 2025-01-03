---
title: Binary Search
date: 2025-01-03
author: Your Name
cell_count: 4
score: 0
---

---
title: "Binary Search"
author: "Rj"
date: 2019-04-20
description: "List Test"
type: technical_note
draft: false
---

```python
def binary_search(lys, val):  
    first = 0
    last = len(lys)-1
    index = -1
    while (first <= last) and (index == -1):
        mid = (first+last)//2
        if lys[mid] == val:
            index = mid
        else:
            if val<lys[mid]:
                last = mid -1
            else:
                first = mid +1
    return index
```


```python
list = [1, 2, 5, 6]

print(binary_search(list, 5))
```

    2



```python

```


---
**Score: 0**