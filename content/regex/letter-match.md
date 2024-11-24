---
title: Letter-Match
date: 2024-11-24
author: Your Name
cell_count: 5
score: 5
---

---
title: "Letter Match"
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
contents = [
    "AB23",
    "A2B3", 
    "DE09",
    "MN90",
    "XYi9",
    "XY90"
]
```


```python
for content in contents:
    regex_pattern = "(?:AB|DE|XY)\d+" 
    # starts with AB or DE; should contain one or more number

    m = re.match(regex_pattern, content)

    if(m):
        print('matched : '+content)
```

    matched : AB23
    matched : DE09
    matched : XY90



```python

```


---
**Score: 5**