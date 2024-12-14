---
title: Counter-Simple
date: 2024-12-14
author: Your Name
cell_count: 8
score: 5
---

---
title: "Counter Simple"
author: "Rj"
date: 2019-04-20
description: "List Test"
type: technical_note
draft: false
---

```python
from collections import Counter
```


```python
a = Counter("Hello there, How are you")
```


```python
a
```




    Counter({' ': 4,
             ',': 1,
             'H': 2,
             'a': 1,
             'e': 4,
             'h': 1,
             'l': 2,
             'o': 3,
             'r': 2,
             't': 1,
             'u': 1,
             'w': 1,
             'y': 1})




```python
def isin(a, b):
    return not Counter(a) - Counter(b)
```


```python
isin("hel my frend", "hello my friend")
```




    True



More:
    
    https://stackoverflow.com/questions/56189821/how-to-check-if-a-string-is-a-substring-of-another-even-if-not-in-order


```python

```


---
**Score: 5**