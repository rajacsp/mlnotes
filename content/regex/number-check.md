---
title: Number-Check
date: 2025-01-04
author: Your Name
cell_count: 5
score: 5
---

---
title: "Number Check"
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
pattern = re.compile("^([0-9]+)+$")

content  = "s23434"

if(pattern.match(content)):
    print(pattern.match(content).pos)
else:
    print('not matched')
```

    not matched



```python
content  = "23434"

if(pattern.match(content)):
    print('matched at : ', pattern.match(content).pos)
else:
    print('not matched')
```

    matched at :  0



```python

```


---
**Score: 5**