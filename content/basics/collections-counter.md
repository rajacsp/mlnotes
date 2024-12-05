---
title: Collections-Counter
date: 2024-12-05
author: Your Name
cell_count: 6
score: 5
---

---
title: "Collections Counter"
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
cnt = Counter()

for word in ['Toronto', 'Montreal', 'Montreal', 'Waterloo', 'Toronto', 'Toronto']:
    cnt[word] += 1
```


```python
cnt
```




    Counter({'Montreal': 2, 'Toronto': 3, 'Waterloo': 1})




```python
type(cnt)
```




    collections.Counter




```python

```


---
**Score: 5**