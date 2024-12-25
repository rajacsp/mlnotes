---
title: Regex-Groups
date: 2024-12-25
author: Your Name
cell_count: 4
score: 0
---

---
title: "Regex Groups"
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
names = ['A2B8']

for name in names:
    m = re.match("^[A-Z]\d[A-Z]\d", name)

    if(m):
        print(m.groups())
        print('matched : ', name)
```

    ()
    matched :  A2B8



```python

```


---
**Score: 0**