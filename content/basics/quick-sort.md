---
title: Quick-Sort
date: 2024-12-04
author: Your Name
cell_count: 4
score: 0
---

---
title: "Quick Sorting"
author: "Rj"
date: 2019-04-20
description: "List Test"
type: technical_note
draft: false
---

```python
def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quicksort(left) + middle + quicksort(right)
```


```python
print(quicksort([3,6,8,10,1,2,1]))
```

    [1, 1, 2, 3, 6, 8, 10]



```python

```


---
**Score: 0**