---
title: Levenshtein-Distance
date: 2024-12-03
author: Your Name
cell_count: 7
score: 5
---

---
title: "Levenshtein Distance"
author: "Rj"
date: 2019-04-21
description: "-"
type: technical_note
draft: false
---

```python
import numpy as np
```


```python
def levenshtein_distance(s, t):
    if s == "":
        return len(t)

    if t == "":
        return len(s)
        
    if s[-1] == t[-1]:
        cost = 0
    else:
        cost = 1
       
    res = min([levenshtein_distance(s[:-1], t)+1,
               levenshtein_distance(s, t[:-1])+1, 
               levenshtein_distance(s[:-1], t[:-1]) + cost])
    return res
```


```python
levenshtein_distance("Python", "Pithon")
```




    1




```python
levenshtein_distance("Canada", "Kanata")
```




    2




```python
levenshtein_distance("Australia", "Boston")
```




    7




```python
levenshtein_distance("Peter", "Beat It")
```




    5




---
**Score: 5**