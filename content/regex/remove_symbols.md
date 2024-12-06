---
title: Remove Symbols
date: 2024-12-06
author: Your Name
cell_count: 7
score: 5
---

---
title: "Remove Symbols"
author: "Raja CSP Raman"
date: 2019-04-20
description: "-"
type: technical_note
draft: false
---

```python
content = "This device is costing only 12.89$. This is fantastic!"
```


```python
content
```




    'This device is costing only 12.89$. This is fantastic!'




```python
import re
```


```python
re.sub(r'[^\w]', ' ', content)
```




    'This device is costing only 12 89   This is fantastic '



Note:

\w will match alphanumeric characters and underscores

[^\w] will match anything that's not alphanumeric or underscore


```python

```


---
**Score: 5**