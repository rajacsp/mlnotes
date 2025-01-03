---
title: Simple-Match
date: 2025-01-03
author: Your Name
cell_count: 7
score: 5
---

---
title: "Simple Match"
author: "Raja CSP Raman"
date: 2019-04-20
description: "-"
type: technical_note
draft: false
---

```python
import re
```


```python
content = "Eminem means positive"
```


```python
a = re.search('^Em.*ve$', content)
```


```python
if(a):
    print('matched')
else:
    print('not matched')
```

    matched


More situations


- Match Canadian postal code
- Phone number
- Start with /home
- Contains /User/raja


```python

```


---
**Score: 5**