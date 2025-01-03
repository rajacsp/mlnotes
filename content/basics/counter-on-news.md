---
title: Counter-On-News
date: 2025-01-03
author: Your Name
cell_count: 4
score: 0
---

---
title: "Counter On News"
author: "Rj"
date: 2019-04-20
description: "List Test"
type: technical_note
draft: false
---

```python
import re
from collections import Counter
```


```python
words = re.findall(r'\w+', open('../../../assets/news.txt').read().lower())
Counter(words).most_common(10)
```




    [('a', 37),
     ('and', 36),
     ('to', 30),
     ('the', 27),
     ('that', 24),
     ('of', 18),
     ('employees', 17),
     ('is', 14),
     ('in', 14),
     ('as', 13)]




```python

```


---
**Score: 0**